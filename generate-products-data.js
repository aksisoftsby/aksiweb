/**
 * Generator _data/products.json.
 *
 * Halaman produk (/produk/*) berada di collection "pages" yang didefinisikan
 * di _config.yml. Karena collection itu menutupi `site.pages`, template tidak
 * bisa andal mengambil daftar produk dari sana; hasilnya nil dan build gagal
 * dengan "Cannot sort a null object".
 *
 * Solusinya: front matter halaman produk diekstrak ke file data, lalu template
 * membacanya lewat `site.data.products` — jalur yang selalu tersedia di Jekyll.
 *
 * Jalankan: node generate-products-data.js
 * Jalankan ulang setiap kali front matter halaman produk berubah.
 */
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const SRC = __dirname;
const PAGES_DIR = path.join(SRC, 'pages');
const OUT = path.join(SRC, '_data', 'products.json');

function readFrontMatter(file) {
  const raw = fs.readFileSync(file, 'utf8');
  const m = raw.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return null;
  try {
    return yaml.load(m[1]) || {};
  } catch (err) {
    console.error(`YAML tidak valid: ${file}\n  ${err.message}`);
    return null;
  }
}

const products = [];

for (const f of fs.readdirSync(PAGES_DIR).sort()) {
  if (!f.endsWith('.md')) continue;
  const data = readFrontMatter(path.join(PAGES_DIR, f));
  if (!data || data.layout !== 'product') continue;

  products.push({
    // Nama field sengaja sama dengan front matter halaman produk supaya
    // template di index.html dan pages/portfolio.md tidak perlu diubah.
    product_name: data.product_name || '',
    product_initial: data.product_initial || '',
    product_label: data.product_label || 'Produk',
    product_key: data.product_key || '',
    product_order: Number(data.product_order) || 99,
    product_domain: data.product_domain || '',
    product_url: data.product_url || '',
    logo: data.logo || '',
    url: data.permalink || '',
    hero_image: data.hero_image || '',
    hero_alt: data.hero_alt || '',
    description: data.description || '',
  });
}

products.sort((a, b) => a.product_order - b.product_order);

fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(products, null, 2) + '\n');

console.log(`Wrote ${products.length} products to _data/products.json`);
for (const p of products) console.log(` - ${p.product_order} ${p.product_name} -> ${p.url}`);