/**
 * Generator katalog eBook.
 *
 * Mengikuti pola generate.js (website): fetch API -> normalisasi -> tulis
 * `_data/ebooks.json` (dipakai katalog /ebook/) + halaman detail
 * `_ebooks/{slug}.md` (collection Jekyll -> /ebook/{slug}/).
 *
 * Jalankan: node generate-ebooks-data.js
 * Jalankan ulang setiap kali ingin menyegarkan data dari API.
 */
const fs = require('fs');
const path = require('path');

// ============================================================
// CONFIGURATION
// ============================================================
const CONFIG = {
  baseUrl: 'https://template.aksisoft.web.id',
  listingApi: 'https://template.aksisoft.web.id/api/ebook',
  dataFile: '_data/ebooks.json',
  detailDir: '_ebooks',
  pageSize: 48,               // API membatasi limit maksimal 48
  // Ketika true, hapus halaman detail yang slug-nya sudah tidak ada di API.
  cleanStale: false,
};
// ============================================================

const ROOT = path.resolve(__dirname);
const DEBUG = process.argv.includes('--debug');
let warned = false;

function log(...a) { console.log(...a); }
function debug(...a) { if (DEBUG) console.log('  [debug]', ...a); }
function warn(msg) { anyWarn = true; console.warn('WARNING: ' + msg); }
let anyWarn = false;

/** YAML-safe quoted string (selalu pakai tanda kutip ganda + escape). */
function q(value) {
  return '"' + String(value == null ? '' : value)
    .replace(/\\/g, '\\\\')
    .replace(/"/g, '\\"')
    .replace(/\r?\n/g, ' ')
    .trim() + '"';
}

async function fetchJson(url) {
  const res = await fetch(url, { headers: { Accept: 'application/json' } });
  if (!res.ok) throw new Error(`API HTTP ${res.status} untuk ${url}`);
  const text = await res.text();
  try {
    return JSON.parse(text);
  } catch {
    throw new Error(`Respons bukan JSON: ${url}`);
  }
}

function absoluteUrl(u) {
  if (!u || typeof u !== 'string') return '';
  if (/^https?:\/\//i.test(u)) return u;
  return CONFIG.baseUrl + (u.startsWith('/') ? u : '/' + u);
}

function toArray(raw) {
  if (Array.isArray(raw)) return raw;
  if (typeof raw === 'string') {
    try {
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch {
      return [];
    }
  }
  return [];
}

function formatDate(ts) {
  if (!ts) return '';
  const d = new Date(Number(ts) * 1000);
  if (Number.isNaN(d.getTime())) return '';
  return d.toISOString().slice(0, 10);
}

/** Normalisasi 1 item API -> struktur yang dipakai template. */
function normalizeEbook(item) {
  // `screenshot_urls` sudah berupa path lengkap; `screenshots`/`screenshot`
  // hanya nama berkas sehingga perlu diberi prefix folder screenshot.
  const rawShots = toArray(item.screenshot_urls).length
    ? toArray(item.screenshot_urls)
    : [...toArray(item.screenshots), ...toArray(item.screenshot)]
      .map((s) => (typeof s === 'string' && s && !s.includes('/') ? `/ebook/screenshot/${s}` : s));
  const cover = item.cover_url || item.cover || item.image || '';
  return {
    id: item.id,
    slug: item.slug || '',
    // `name` adalah judul produk, `title` dipakai konsisten dengan katalog website.
    name: item.name || '',
    title: item.name || item.title || '',
    description: (item.description || '').trim(),
    content: item.content || '',
    category: 'Ebook',
    price: Number(item.price) || 0,
    compare_price: Number(item.compare_price) || 0,
    rating: Number(item.rating) || 0,
    rating_count: Number(item.rating_count) || 0,
    cover: absoluteUrl(cover),
    thumbnail: absoluteUrl(cover),
    screenshots: rawShots.map(absoluteUrl),
    buy_url: item.lynk_id || item.mayar || '',
    mayar_url: item.mayar || '',
    detail_url: item.detail_url || '',
    created_at: formatDate(item.created_date),
    updated_at: formatDate(item.update_date),
    status: 'published',
    type: 'ebook',
    // URL halaman detail di situs ini (collection `ebooks`),
    // sejajar dengan `url` pada _data/websites.json.
    url: `/ebook/${item.slug || ''}/`,
  };
}

/** Ambil semua halaman listing sampai habis. */
async function fetchAll() {
  const items = [];
  let page = 1;
  let totalPages = 1;
  do {
    const url = `${CONFIG.listingApi}?page=${page}&limit=${CONFIG.pageSize}`;
    const json = await fetchJson(url);
    if (!json || json.success === false || !Array.isArray(json.data)) {
      throw new Error(`Struktur respons tidak dikenal di halaman ${page}`);
    }
    items.push(...json.data);
    const meta = json.meta || {};
    totalPages = Number(meta.totalPages) || 1;
    debug(`halaman ${page}/${totalPages} -> ${json.data.length} item`);
    page += 1;
  } while (page <= totalPages);
  return items;
}

function writeDetailPage(ebook) {
  const fm = [
    '---',
    'layout: ebook',
    `slug: ${q(ebook.slug)}`,
    `title: ${q(ebook.title)}`,
    `description: ${q(ebook.description)}`,
    'category: "Ebook"',
    `image: ${q(ebook.thumbnail)}`,
    `buy_url: ${q(ebook.buy_url)}`,
    `mayar_url: ${q(ebook.mayar_url)}`,
    `price: ${ebook.price}`,
    `compare_price: ${ebook.compare_price}`,
    `rating: ${ebook.rating}`,
    `rating_count: ${ebook.rating_count}`,
    `created_at: ${q(ebook.created_at)}`,
    `updated_at: ${q(ebook.updated_at)}`,
    `screenshots: ${JSON.stringify(ebook.screenshots)}`,
    '---',
    '',
    // Konten dari API sudah berupa Markdown; Jekyll (kramdown) yang merender.
    ebook.content || ebook.description,
    '',
  ].join('\n');
  fs.writeFileSync(path.join(ROOT, CONFIG.detailDir, `${ebook.slug}.md`), fm, 'utf8');
}

async function main() {
  log('Fetch katalog eBook dari ' + CONFIG.listingApi);
  const raw = await fetchAll();
  log(`Diterima ${raw.length} item dari API`);

  const seen = new Set();
  const ebooks = [];
  for (const item of raw) {
    const e = normalizeEbook(item);
    if (!e.slug) { warn(`Item tanpa slug dilewati: ${JSON.stringify(item).slice(0, 80)}`); continue; }
    if (seen.has(e.slug)) { warn(`Slug duplikat dilewati: ${e.slug}`); continue; }
    seen.add(e.slug);
    ebooks.push(e);
  }
  ebooks.sort((a, b) => (b.updated_at || '').localeCompare(a.updated_at || '') || a.title.localeCompare(b.title));

  fs.mkdirSync(path.dirname(path.join(ROOT, CONFIG.dataFile)), { recursive: true });
  fs.writeFileSync(path.join(ROOT, CONFIG.dataFile), JSON.stringify(ebooks, null, 2) + '\n', 'utf8');
  log(`Wrote ${ebooks.length} ebook -> ${CONFIG.dataFile}`);

  fs.mkdirSync(path.join(ROOT, CONFIG.detailDir), { recursive: true });
  let written = 0;
  for (const e of ebooks) {
    writeDetailPage(e);
    written += 1;
  }
  log(`Wrote ${written} halaman detail -> ${CONFIG.detailDir}/`);

  if (CONFIG.cleanStale) {
    const keep = new Set(ebooks.map((e) => `${e.slug}.md`));
    for (const f of fs.readdirSync(path.join(ROOT, CONFIG.detailDir))) {
      if (f.endsWith('.md') && !keep.has(f)) {
        fs.unlinkSync(path.join(ROOT, CONFIG.detailDir, f));
        log(`  hapus stale: ${f}`);
      }
    }
  }

  const noCover = ebooks.filter((e) => !e.thumbnail).length;
  if (noCover) warn(`${noCover} ebook tanpa cover`);
  log(anyWarn ? '\nSELESAI (dengan peringatan)' : '\nSELESAI');
}

main().catch((err) => {
  console.error('GAGAL: ' + err.message);
  process.exit(1);
});
