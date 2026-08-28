const fs = require('fs');
const path = require('path');

// ============================================================
// CONFIGURATION - ubah pengaturan di sini saja
// ============================================================
const CONFIG = {
  baseUrl: 'https://template.aksisoft.web.id',
  listingApi: 'https://template.aksisoft.web.id/api/websites',
  detailApiBySlug: 'https://template.aksisoft.web.id/api/websites/slug/',
  detailApiFallback: 'https://template.aksisoft.web.id/api/v1/websites/',
  imageBaseUrl: 'https://template.aksisoft.web.id',
  dataFile: '_data/websites.json',        // katalog data (dipakai halaman katalog)
  detailDir: '_websites',                 // collection Jekyll -> /website/{slug}/
  concurrency: 5,
  buildAfterGenerate: false,              // ubah true untuk jekyll build otomatis
  defaultCategory: 'HTML Template',
  fallbackImage: '/assets/img/aksisoft-monogram.png'
};
// ============================================================

const DEBUG = process.argv.includes('--debug') || process.argv.includes('debug');
const CLEAN = process.argv.includes('--clean') || process.argv.includes('clean');
const BUILD = process.argv.includes('--build') || process.argv.includes('build');

const ROOT = path.resolve(__dirname);
const counters = { generated: 0, failed: 0, skipped: 0, cleaned: 0 };
const warnings = [];

function log(...a) { console.log(...a); }
function debug(...a) { if (DEBUG) console.log('  [debug]', ...a); }
function warn(msg) { warnings.push(msg); console.log('WARNING: ' + msg); }

// ---------- utilities ----------
async function fetchJson(url) {
  let res;
  try {
    res = await fetch(url, { headers: { 'Accept': 'application/json' } });
  } catch (e) {
    throw new Error(`Network error for ${url}: ${e.message}`);
  }
  if (!res.ok) throw new Error(`API returned HTTP ${res.status} for ${url}`);
  const text = await res.text();
  try { return JSON.parse(text); }
  catch { throw new Error(`Invalid JSON response from ${url}`); }
}

function absoluteUrl(u) {
  if (!u || typeof u !== 'string') return '';
  if (/^https?:\/\//i.test(u)) return u;
  if (u.startsWith('/')) return CONFIG.imageBaseUrl + u;
  return CONFIG.imageBaseUrl + '/' + u;
}

/** Parse media/gallery field yang bisa berupa JSON string, object, atau array. */
function parseMedia(raw) {
  let obj = raw;
  if (typeof raw === 'string') {
    try { obj = JSON.parse(raw); }
    catch { return { desktop: [], mobile: [], code: [], all: raw ? [raw] : [] }; }
  }
  if (Array.isArray(obj)) return { desktop: obj, mobile: [], code: [], all: obj };
  if (!obj || typeof obj !== 'object') return { desktop: [], mobile: [], code: [], all: [] };
  const desktop = Array.isArray(obj.desktop) ? obj.desktop : [];
  const mobile = Array.isArray(obj.mobile) ? obj.mobile : [];
  const code = Array.isArray(obj.code) ? obj.code : [];
  const all = Array.isArray(obj.all) ? obj.all : [...desktop, ...mobile, ...code];
  return { desktop, mobile, code, all };
}

/** Normalisasi item API -> struktur internal konsisten. */
function normalizeWebsite(item) {
  const media = parseMedia(item.media);
  const galleryRaw = item.gallery && typeof item.gallery === 'object' && !Array.isArray(item.gallery) ? item.gallery : null;
  const screenshots = Array.isArray(item.screenshots) && item.screenshots.length
    ? item.screenshots
    : (media.all || []);
  const thumbnail = item.screenshot || item.thumbnail || item.thumbnail_url || item.image ||
    item.image_url || item.cover || item.cover_image || item.featured_image ||
    item.preview || (screenshots[0] || '') || (media.desktop[0] || '');

  const slug = String(item.slug || item.name || '').trim();
  const title = String(item.selling_title || item.title || item.name || slug).trim();

  return {
    id: item.id != null ? String(item.id) : '',
    slug,
    title,
    name: item.name || slug,
    description: String(item.short_description || item.description || '').trim(),
    long_description: String(item.long_description || item.description || '').trim(),
    category: item.category || item.kategori || CONFIG.defaultCategory,
    tags: Array.isArray(item.tags) ? item.tags : [],
    thumbnail: absoluteUrl(thumbnail),
    screenshots: screenshots.map(absoluteUrl).filter(Boolean),
    gallery: {
      desktop: ((galleryRaw && galleryRaw.desktop) || media.desktop).map(absoluteUrl),
      mobile: ((galleryRaw && galleryRaw.mobile) || media.mobile).map(absoluteUrl),
      code: ((galleryRaw && galleryRaw.code) || media.code).map(absoluteUrl)
    },
    demo_url: absoluteUrl(item.demo_url || ''),
    detail_url: item.detail_url || `/website/${slug}`,
    buy_url: item.lynk_id || item.buy_url || item.download_url || '',
    price: item.price != null ? Number(item.price) : null,
    version: item.version || '',
    status: item.status || '',
    updated_at: item.updated_at ? new Date(item.updated_at * 1000).toISOString().slice(0, 10) : ''
  };
}

/** Quote string sebagai YAML double-quoted scalar (JSON encoding kompatibel YAML). */
function yq(s) {
  if (s == null || s === '') return '""';
  if (typeof s === 'number') return String(s);
  return JSON.stringify(String(s));
}

// ---------- concurrency pool ----------
async function runPool(items, worker, limit) {
  const results = new Array(items.length);
  let i = 0;
  async function next() {
    while (i < items.length) {
      const idx = i++;
      try { results[idx] = await worker(items[idx], idx); }
      catch (e) { results[idx] = { error: e }; }
    }
  }
  await Promise.all(Array.from({ length: Math.min(limit, items.length) }, next));
  return results;
}

// ---------- fetch detail dengan fallback endpoint ----------
async function fetchDetail(w) {
  const endpoints = [
    CONFIG.detailApiBySlug + w.slug,
    CONFIG.detailApiFallback + w.slug,
    CONFIG.detailApiFallback + w.id
  ];
  for (const url of endpoints) {
    try {
      debug('detail url:', url);
      const json = await fetchJson(url);
      const data = json && (json.data || json);
      if (data && (data.slug || data.name || data.selling_title)) return { data, url };
    } catch (e) {
      debug('detail gagal:', url, '-', e.message);
    }
  }
  throw new Error('all detail endpoints failed');
}

// ---------- generate detail page ----------
function detailPageContent(w) {
  return [
    '---',
    'layout: website',
    `slug: ${yq(w.slug)}`,
    `title: ${yq(w.title)}`,
    `description: ${yq(w.description)}`,
    `category: ${yq(w.category)}`,
    `image: ${yq(w.thumbnail)}`,
    `demo_url: ${yq(w.demo_url)}`,
    `buy_url: ${yq(w.buy_url)}`,
    `price: ${w.price == null ? 'null' : w.price}`,
    `version: ${yq(w.version)}`,
    `status: ${yq(w.status)}`,
    `updated_at: ${yq(w.updated_at)}`,
    `gallery: ${JSON.stringify(w.gallery)}`,
    `screenshots: ${JSON.stringify(w.screenshots)}`,
    '---',
    '',
    w.long_description ? w.long_description + '\n' : ''
  ].join('\n');
}

function writeDetailPage(w) {
  const dir = path.join(ROOT, CONFIG.detailDir);
  fs.mkdirSync(dir, { recursive: true });
  const file = path.join(dir, `${w.slug}.md`);
  fs.writeFileSync(file, detailPageContent(w), 'utf8');
  counters.generated++;
  log(`       generated: ${CONFIG.detailDir}/${w.slug}.md`);
  debug(`       images: ${w.screenshots.length} screenshots (desktop=${w.gallery.desktop.length} mobile=${w.gallery.mobile.length} code=${w.gallery.code.length})`);
}


// ---------- main ----------
(async () => {
  log('========================================');
  log('Jekyll Website Generator');
  log('========================================');
  debug('API URL:', CONFIG.listingApi);

  // [1] Fetch listing
  log('\nFetching listing...');
  let json;
  try {
    json = await fetchJson(CONFIG.listingApi);
    log('HTTP 200');
  } catch (e) {
    log('ERROR: Failed to fetch listing API');
    log(e.message);
    process.exit(1);
  }
  const rawItems = Array.isArray(json) ? json : (json.data || json.websites || []);
  log(`\nFound: ${rawItems.length} websites`);
  if (!rawItems.length) {
    log('ERROR: Listing API returned 0 items');
    process.exit(1);
  }

  // [2] Normalize + deteksi duplicate slug
  const seen = new Set();
  const websites = [];
  for (const item of rawItems) {
    const w = normalizeWebsite(item);
    if (!w.slug) {
      warn('Website skipped because slug is missing' + (w.title ? ` (${w.title})` : ''));
      counters.skipped++;
      continue;
    }
    if (seen.has(w.slug)) {
      warn(`Duplicate slug detected: ${w.slug} (duplicate dilewati)`);
      counters.skipped++;
      continue;
    }
    seen.add(w.slug);
    w.__raw = item;
    websites.push(w);
  }

  // [3] Fetch detail setiap website (concurrency terbatas)
  log('\nFetching details...');
  const results = await runPool(websites, async (w, idx) => {
    const num = String(idx + 1).padStart(2, '0');
    log(`[${num}/${websites.length}] ${w.title}`);
    log(`       slug: ${w.slug}`);
    try {
      const { data, url } = await fetchDetail(w);
      const merged = normalizeWebsite(Object.assign({}, w.__raw, data, { slug: w.slug, id: w.id }));
      log(`       detail: OK (${url})`);
      writeDetailPage(merged);
      return merged;
    } catch (e) {
      log(`       detail: FAILED (${e.message})`);
      warn(`Failed to fetch detail for ${w.slug}: ${e.message}. Menggunakan data listing.`);
      counters.failed++;
      writeDetailPage(w);
      return w;
    }
  }, CONFIG.concurrency);

  // [4] Simpan data katalog (dipakai halaman katalog statis)
  const catalog = results.map(w => ({
    id: w.id, slug: w.slug, title: w.title, description: w.description,
    category: w.category, tags: w.tags, thumbnail: w.thumbnail,
    screenshots: w.screenshots, gallery: w.gallery,
    demo_url: w.demo_url, buy_url: w.buy_url, price: w.price,
    version: w.version, status: w.status, updated_at: w.updated_at,
    url: `/website/${w.slug}/`
  }));
  const dataDir = path.join(ROOT, path.dirname(CONFIG.dataFile));
  fs.mkdirSync(dataDir, { recursive: true });
  fs.writeFileSync(path.join(ROOT, CONFIG.dataFile), JSON.stringify(catalog, null, 2), 'utf8');
  log(`\nCatalog data: ${CONFIG.dataFile} (${catalog.length} items)`);

  // [5] Cleanup halaman usang (opsional, default OFF)
  if (CLEAN) {
    const dir = path.join(ROOT, CONFIG.detailDir);
    if (fs.existsSync(dir)) {
      const validSlugs = new Set(websites.map(w => w.slug));
      for (const f of fs.readdirSync(dir)) {
        const slug = f.replace(/\.md$/, '');
        if (!validSlugs.has(slug)) {
          fs.unlinkSync(path.join(dir, f));
          counters.cleaned++;
          log(`CLEANED: ${CONFIG.detailDir}/${f} (tidak ada lagi di API)`);
        }
      }
    }
  } else {
    debug('clean mode OFF (gunakan --clean untuk menghapus halaman usang)');
  }

  // [6] Validasi sederhana
  log('\nValidating...');
  const issues = [];
  const slugs = catalog.map(c => c.slug);
  const dupes = slugs.length - new Set(slugs).size;
  if (dupes) issues.push(`${dupes} duplicate slug`);
  catalog.forEach(c => {
    if (!c.title) issues.push(`title kosong: ${c.slug}`);
    if (!c.thumbnail) issues.push(`thumbnail kosong: ${c.slug}`);
    if (!fs.existsSync(path.join(ROOT, CONFIG.detailDir, c.slug + '.md'))) {
      issues.push(`detail page tidak ada: ${c.slug}`);
    }
  });
  if (issues.length) issues.forEach(i => log('VALIDATION: ' + i));
  else log(`OK: ${catalog.length} katalog item, ${catalog.length} detail pages, semua link valid`);

  // [7] Optional jekyll build
  if (BUILD || CONFIG.buildAfterGenerate) {
    log('\nBuilding Jekyll...');
    const { execSync } = require('child_process');
    try {
      execSync('bundle exec jekyll build', { cwd: ROOT, stdio: 'inherit' });
    } catch {
      try {
        execSync('jekyll build', { cwd: ROOT, stdio: 'inherit' });
      } catch {
        log('ERROR: Jekyll build gagal. Pastikan Ruby/Bundler/Jekyll terinstall.');
      }
    }
  }

  // Summary
  log('\n========================================');
  log('DONE');
  log('========================================');
  log(`Catalog : ${catalog.length} items -> ${CONFIG.dataFile}`);
  log(`Details : ${counters.generated} generated -> ${CONFIG.detailDir}/`);
  log(`Failed  : ${counters.failed}`);
  log(`Skipped : ${counters.skipped}`);
  log(`Cleaned : ${counters.cleaned}`);
  if (warnings.length) log(`Warnings: ${warnings.length}`);
})().catch(e => {
  log('ERROR: ' + e.message);
  process.exit(1);
});

