/**
 * Generator artikel SEO Aksisoft.
 *
 * Menghasilkan 200 halaman layanan berbasis keyword ("jasa buat website surabaya",
 * "jasa aplikasi android bandung", dll) untuk kota-kota besar di Jawa & Bali.
 *
 * Sengaja TIDAK memakai collection `posts` (artikel/news) supaya blog tetap
 * bersih: konten ini adalah landing page per keyword, bukan kronologi berita.
 * Dipakai collection `seo_articles` dengan permalink /jasa/:name/.
 *
 * Jalankan: node generate-seo-articles.js
 */
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.join(__dirname, '_seo_articles');

/* ------------------------------------------------------------------ */
/* Data kota: Jawa + Bali                                              */
/* ------------------------------------------------------------------ */
const CITIES = [
  { slug: 'surabaya', name: 'Surabaya', province: 'Jawa Timur' },
  { slug: 'jakarta', name: 'Jakarta', province: 'DKI Jakarta' },
  { slug: 'bandung', name: 'Bandung', province: 'Jawa Barat' },
  { slug: 'semarang', name: 'Semarang', province: 'Jawa Tengah' },
  { slug: 'yogyakarta', name: 'Yogyakarta', province: 'DI Yogyakarta' },
  { slug: 'malang', name: 'Malang', province: 'Jawa Timur' },
  { slug: 'sidoarjo', name: 'Sidoarjo', province: 'Jawa Timur' },
  { slug: 'gresik', name: 'Gresik', province: 'Jawa Timur' },
  { slug: 'kediri', name: 'Kediri', province: 'Jawa Timur' },
  { slug: 'madiun', name: 'Madiun', province: 'Jawa Timur' },
  { slug: 'solo', name: 'Surakarta (Solo)', province: 'Jawa Tengah' },
  { slug: 'magelang', name: 'Magelang', province: 'Jawa Tengah' },
  { slug: 'pekalongan', name: 'Pekalongan', province: 'Jawa Tengah' },
  { slug: 'salatiga', name: 'Salatiga', province: 'Jawa Tengah' },
  { slug: 'bogor', name: 'Bogor', province: 'Jawa Barat' },
  { slug: 'bekasi', name: 'Bekasi', province: 'Jawa Barat' },
  { slug: 'depok', name: 'Depok', province: 'Jawa Barat' },
  { slug: 'cilacap', name: 'Cilacap', province: 'Jawa Tengah' },
  { slug: 'probolinggo', name: 'Probolinggo', province: 'Jawa Timur' },
  { slug: 'denpasar', name: 'Denpasar', province: 'Bali' },
];

const BALI_REGIONS = [
  { slug: 'badung', name: 'Kabupaten Badung' },
  { slug: 'gianyar', name: 'Kabupaten Gianyar' },
  { slug: 'tabanan', name: 'Kabupaten Tabanan' },
  { slug: 'jembrana', name: 'Kabupaten Jembrana' },
  { slug: 'buleleng', name: 'Kabupaten Buleleng' },
  { slug: 'karangasem', name: 'Karangasem' },
  { slug: 'bangli', name: 'Kabupaten Bangli' },
  { slug: 'klungkung', name: 'Kabupaten Klungkung' },
];

/* ------------------------------------------------------------------ */
/* 10 template keyword                                                 */
/* ------------------------------------------------------------------ */
const SERVICES = [
  {
    slug: 'jasa-buat-website',
    label: 'Jasa Pembuatan Website',
    short: 'jasa pembuatan website',
    h1: (c) => `Jasa Buat Website ${c} — Desain Profesional, SEO Ready`,
    title: (c) => `Jasa Buat Website ${c} | Pembuatan Website Profesional`,
    desc: (c) =>
      `Jasa buat website ${c} dengan desain profesional, cepat, dan SEO-friendly. ` +
      `Cocok untuk UMKM, company profile, katalog produk, dan blog bisnis. ` +
      `Harga transparan, pengerjaan cepat, revisi sesuai paket.`,
    ctaText: 'Konsultasi Gratis',
    ctaUrl: '/kontak/?subject=Jasa%20Buat%20Website',
  },
  {
    slug: 'jasa-aplikasi-android',
    label: 'Jasa Aplikasi Android',
    short: 'jasa aplikasi Android',
    slug2: true,
    h1: (c) => `Jasa Aplikasi Android ${c} — Custom App Siap Rilis Google Play`,
    title: (c) => `Jasa Aplikasi Android ${c} | Custom App Developer`,
    desc: (c) =>
      `Jasa aplikasi Android ${c} untuk bisnis, toko, dan layanan lokal. ` +
      `Dibangun custom sesuai alur kerja Anda, diuji di perangkat nyata, ` +
      `dan disiapkan untuk rilis ke Google Play.`,
    ctaText: 'Konsultasi Android',
    ctaUrl: '/kontak/?subject=Jasa%20Aplikasi%20Android',
  },
  {
    slug: 'jasa-aplikasi-custom',
    label: 'Jasa Aplikasi Custom',
    short: 'jasa aplikasi custom',
    h1: (c) => `Jasa Aplikasi Custom ${c} — Sistem Sesuai Alur Kerja Anda`,
    title: (c) => `Jasa Aplikasi Custom ${c} | Sistem dan Dashboard Custom`,
    desc: (c) =>
      `Jasa aplikasi custom ${c}: dashboard internal, sistem operasional, ` +
      `booking, inventori, sampai integrasi API pihak ketiga. ` +
      `Dirancang dari alur kerja nyata, bukan template generik.`,
    ctaText: 'Diskusikan Kebutuhan',
    ctaUrl: '/kontak/?subject=Jasa%20Aplikasi%20Custom',
  },
  {
    slug: 'jasa-website-murah',
    label: 'Jasa Website Murah',
    short: 'jasa website murah',
    h1: (c) => `Jasa Website Murah ${c} — Harga Ramah, Kualitas Profesional`,
    title: (c) => `Jasa Website Murah ${c} | Mulai Rp 1.500.000`,
    desc: (c) =>
      `Jasa website murah ${c} mulai Rp 1.500.000. Cocok untuk UMKM dan usaha baru ` +
      `yang butuh website resmi, cepat, dan mudah dikelola, tanpa biaya tersembunyi.`,
    ctaText: 'Lihat Paket Harga',
    ctaUrl: '/kontak/?subject=Jasa%20Website%20Murah',
  },
  {
    slug: 'jasa-company-profile',
    label: 'Jasa Website Company Profile',
    short: 'jasa company profile',
    h1: (c) => `Jasa Website Company Profile ${c} — Wajah Digital Perusahaan Anda`,
    title: (c) => `Jasa Company Profile ${c} | Website Profil Perusahaan`,
    desc: (c) =>
      `Jasa company profile ${c} untuk perusahaan, kontraktor, dan praktisi. ` +
      `Menggabungkan profil, portofolio, katalog produk, dan kontak dalam satu ` +
      `website yang profesional dan mudah dipercaya calon pelanggan.`,
    ctaText: 'Konsultasi Company Profile',
    ctaUrl: '/kontak/?subject=Jasa%20Company%20Profile',
  },
  {
    slug: 'jasa-landing-page',
    label: 'Jasa Landing Page',
    short: 'jasa landing page',
    h1: (c) => `Jasa Landing Page ${c} — Satu Halaman, Satu Tujuan Konversi`,
    title: (c) => `Jasa Landing Page ${c} | Halaman Penjual yang Efektif`,
    desc: (c) =>
      `Jasa landing page ${c} yang fokus converting: satu pesan, satu aksi. ` +
      `Cocok untuk kampanye iklan, event, dan penawaran terbatas, dengan analytics ` +
      `agar Anda tahu halaman mana yang bekerja.`,
    ctaText: 'Buat Landing Page',
    ctaUrl: '/kontak/?subject=Jasa%20Landing%20Page',
  },
  {
    slug: 'jasa-toko-online',
    label: 'Jasa Toko Online',
    short: 'jasa toko online',
    h1: (c) => `Jasa Toko Online ${c} — Jual Produk Secara Digital`,
    title: (c) => `Jasa Toko Online ${c} | E-Commerce dan Katalog Produk`,
    desc: (c) =>
      `Jasa toko online ${c} untuk produsen, reseller, dan UMKM. ` +
      `Katalog produk rapi, pembayaran mudah, dan checkout yang tidak membuat ` +
      `calon pembeli berhenti di tengah jalan.`,
    ctaText: 'Konsultasi Toko Online',
    ctaUrl: '/kontak/?subject=Jasa%20Toko%20Online',
  },
  {
    slug: 'jasa-seo-lokal',
    label: 'Jasa SEO Lokal',
    short: 'jasa SEO lokal',
    h1: (c) => `Jasa SEO ${c} — Muncul di Pencarian Lokal`,
    title: (c) => `Jasa SEO ${c} | Optimasi Pencarian Lokal dan Google Maps`,
    desc: (c) =>
      `Jasa SEO ${c} untuk menaikkan visibilitas di pencarian lokal: optimasi on-page, ` +
      `Google Business Profile, dan backlink lokal. Cocok untuk bisnis yang mengandalkan ` +
      `pelanggan dari area sekitar.`,
    ctaText: 'Audit SEO Gratis',
    ctaUrl: '/kontak/?subject=Jasa%20SEO%20Lokal',
  },
  {
    slug: 'redesign-website',
    label: 'Jasa Redesign Website',
    short: 'jasa redesign website',
    h1: (c) => `Jasa Redesign Website ${c} — Tampilan Lama, Performa Baru`,
    title: (c) => `Jasa Redesign Website ${c} | Refresh Tampilan dan Performa`,
    desc: (c) =>
      `Jasa redesign website ${c} untuk website yang terasa berat, usang, atau tidak ` +
      `mengubah pengunjung menjadi calon pelanggan. Tampilan, kecepatan, dan alur isi ` +
      `diperbarui tanpa mengubah bagian yang sudah bekerja baik.`,
    ctaText: 'Evaluasi Website',
    ctaUrl: '/kontak/?subject=Jasa%20Redesign%20Website',
  },
  {
    slug: 'jasa-sistem-custom',
    label: 'Jasa Sistem Custom dan Integrasi',
    short: 'jasa sistem custom',
    h1: (c) => `Jasa Sistem Custom ${c} — Otomasi Proses yang Sering Manual`,
    title: (c) => `Jasa Sistem Custom ${c} | Integrasi API dan Otomasi Kerja`,
    desc: (c) =>
      `Jasa sistem custom ${c} untuk inventori, absensi, operasional, dan integrasi API. ` +
      `Menghemat jam kerja admin, mengurangi salah input, dan memberi data operasional ` +
      `yang bisa ditelusuri.`,
    ctaText: 'Konsultasi Sistem',
    ctaUrl: '/kontak/?subject=Jasa%20Sistem%20Custom',
  },
];

/* ------------------------------------------------------------------ */
const BRAND_PHONE = '+62-813-3520-6389';

const RELATED = [
  { title: 'Jasa Pembuatan Website', url: '/layanan/website-static/' },
  { title: 'Jasa Website Dinamis dan CMS', url: '/layanan/website-news-dynamic/' },
  { title: 'Jasa Aplikasi Custom dan Android', url: '/layanan/aplikasi-custom-android/' },
  { title: 'Jasa Edit Video', url: '/layanan/video-editing/' },
  { title: 'Jasa Email Marketing', url: '/layanan/email-marketing/' },
  { title: 'Jasa Google Ads', url: '/layanan/google-ads/' },
  { title: 'Jasa Social Media Ads', url: '/layanan/social-media-ads/' },
  { title: 'Produk Aksisoft', url: '/produk/' },
  { title: 'Portfolio Kami', url: '/portfolio/' },
  { title: 'Hubungi Kami', url: '/kontak/' },
];

/* ------------------------------------------------------------------ */
/* Catatan lokal per kota (baris pembuka yang terasa spesifik)          */
/* ------------------------------------------------------------------ */
function localityNote(city) {
  switch (city.slug) {
    case 'surabaya':
      return 'Seiring tumbuhnya UMKM dan industri kreatif di Surabaya, banyak bisnis yang dulu '
        + 'andalkan rekomendasi dari kerabat kini perlu kanal digital sendiri agar tetap relevan '
        + 'saat pelanggan membandingkan pilihan sebelum membeli.';
    case 'jakarta':
      return 'Pasar yang kompetitif di Jakarta menuntut keberadaan digital yang jelas. Karena banyak '
        + 'orang pertama kali mengenal sebuah brand lewat pencarian atau peta lokal, website yang '
        + 'terbaca dengan baik sering menjadi filter sebelum mereka pernah bertemu Anda secara langsung.';
    case 'bandung':
      return 'Bandung memiliki ekosistem startup, kampus, dan komunitas kreatif yang aktif. Untuk '
        + 'bisnis di sini, website perlu tampil modern sekaligus tetap informatif bagi audiens '
        + 'yang luas, dari mahasiswa dan pelanggan individu sampai mitra korporat.';
    case 'denpasar':
      return 'Denpasar dan sekitarnya menerima banyak pengunjung setiap tahun. Website berbahasa '
        + 'Indonesia dengan informasi yang tersusun rapi sangat membantu bisnis lokal maupun '
        + 'pengelola kawasan wisata untuk menemukan informasi sebelum pengunjung datang.';
    case 'semarang':
      return 'Semarang punya kombinasi unik antara industri, perdagangan, dan wisata kota. Website '
        + 'yang menjelaskan penawaran dengan jelas sering menjadi nilai tambah tersendiri di sini.';
    default:
      return `Di ${city.name}, perilaku belanja sudah banyak yang bergeser ke digital. Bisnis yang `
        + 'cepat menyesuaikan biasanya punya informasi yang mudah diakses kapan saja oleh calon '
        + 'pelanggan, tanpa harus menunggu jam operasional.';
  }
}

/* ------------------------------------------------------------------ */
/* Isi artikel                                                         */
/* ------------------------------------------------------------------ */
function buildBody(svc, city) {
  const c = city.name;
  const short = svc.short;

  return `
## Kenapa ${short} di ${c} dibutuhkan

Banyak bisnis di ${c} sudah punya produk atau layanan yang layak, tetapi belum punya tempat yang
terbuka untuk menjelaskannya secara online. ${svc.label} di ${c} menjawab masalah tersebut: satu
ruang untuk menjelaskan penawaran, membangun kepercayaan, dan mengubah pengunjung menjadi calon
pelanggan yang menghubungi Anda.

${localityNote(city)}

### Yang Anda dapatkan dari layanan ini

- Struktur halaman yang mengikuti urutan keputusan calon pembeli
- Tampilan yang menyesuaikan layar ponsel, tablet, dan desktop
- Kecepatan muat halaman yang baik, sehingga pengunjung tidak pergi sebelum selesai membaca
- Kanal kontak yang mudah dijangkau: WhatsApp, telepon, dan formulir
- Fondasi SEO agar halaman mudah ditemukan lewat mesin pencari

## Cakupan layanan di ${c}

Tidak ada satu paket yang cocok untuk semua bisnis. Ruang lingkup ditentukan berdasarkan kondisi
bisnis Anda sekarang, bukan sekadar jumlah halaman.

### Tahap 1 — Fondasi

Membangun kerangka: halaman utama, halaman layanan, dan halaman kontak. Pada tahap ini struktur
konten sudah selesai, sehingga halaman berikutnya jauh lebih mudah ditambahkan.

### Tahap 2 — Pengalaman Detail

Bagian yang paling sering menjadi alasan pembeli berhenti: katalog produk, portofolio, testimoni,
atau alur pemesanan. Bagian ini dirancang agar informasinya mudah dipindai, bukan sekadar pajangan.

### Tahap 3 — Pematangan

Optimalisasi kecepatan, meta description, struktur data, serta pengukuran konversi, supaya Anda
tahu halaman mana yang bekerja dan mana yang perlu diperbaiki.

## Berapa biaya ${short} di ${c}?

Biaya bergantung pada ruang lingkup, bukan pada daftar harga tetap. Hal yang paling memengaruhi
estimasi:

- Jumlah halaman dan kedalaman informasi di tiap halaman
- Integrasi dengan sistem yang sudah Anda pakai
- Tingkat custom design, atau memakai basis yang sudah tersedia
- Kebutuhan pengelolaan konten oleh tim internal Anda

Untuk gambaran kasar, paket dasar umumnya sudah cukup untuk landing page maupun profil bisnis
sederhana. Untuk sistem yang lebih kompleks, estimasi diberikan setelah sesi konsultasi singkat.

> **Catatan jujur.** Harga yang jauh lebih murah daripada pasar biasanya punya bagian yang tidak
> termasuk, misalnya domain, hosting, perawatan, atau revisi. Tanyakan daftar termasuk dan tidak
> termasuk sebelum menyetujui anggaran.

## Proses kerja bersama Aksisoft

1. **Konsultasi awal.** Kami memahami bisnis, target audiens, dan fokus utama Anda.
2. **Rancangan struktur.** Daftar halaman dan poin penting disepakati tertulis.
3. **Desain dan pengerjaan.** Mulai dari kerangka, lalu diisi konten yang Anda siapkan.
4. **Review dan revisi.** Ada kesempatan mengoreksi sebelum halaman tayang.
5. **Serah terima.** Dokumentasi singkat, panduan penggunaan, dan pendampingan awal.

## Mengapa Aksisoft Media untuk ${c}?

Kami bekerja dengan bisnis di ${c} dan sekitarnya, mulai dari UMKM, kontraktor, praktisi, sampai
retailer. Pendekatan kami berawal dari kebutuhan kerja nyata, bukan sekadar membuat halaman yang
cantik tetapi tidak menjalankan fungsi bisnis.

- **Harga transparan.** Estimasi dibahas sebelum pekerjaan dimulai.
- **Komunikasi jelas.** Progres dilaporkan pada titik yang disepakati, bukan menghilang di tengah jalan.
- **Revisi tersedia.** Revisi minor termasuk sesuai paket.
- **Dukungan setelah tayang.** Tidak ditinggalkan begitu proyek selesai.

## Pertanyaan yang sering diajukan

### Berapa lama pengerjaannya?

Umumnya 1–3 minggu untuk paket standar, dan lebih lama untuk proyek custom atau sistem berskala
besar. Estimasi akurat diberikan setelah spesifikasi disepakati.

### Apakah saya bisa mengelola sendiri nanti?

Bisa. Untuk website statis, seluruh konten dapat Anda ubah sendiri. Untuk sistem dinamis, kami
sertakan dashboard beserta panduan operasional.

### Bisa memakai domain sendiri?

Bisa. Anda cukup menyediakan akses domain, tim teknis kami yang menangani pengaturannya. Aset
tetap tercatat atas nama Anda.

### Apakah harga termasuk domain dan hosting?

Belum. Biaya domain dan hosting dibayar langsung kepada penyedia, sehingga Anda memiliki kontrol
penuh atas aset digital sendiri. Kami membantu proses pengaturannya.

### Bagaimana cara memulai?

Kirim brief singkat, atau sekadar jelaskan kebutuhan Anda lewat halaman kontak. Kami akan
menindaklanjuti dengan pertanyaan yang perlu diperjelas sebelum menyusun estimasi.

## Penutup

Mulailah dari kebutuhan yang paling terasa. Perubahan kecil yang dikerjakan dengan benar biasanya
memberi dampak lebih besar daripada proyek besar yang terus ditunda. Kalau Anda sudah punya rencana
di ${c}, hari yang bagus untuk mulainya adalah ketika Anda sudah yakin untuk mulai, dan kami siap
mehidupkannya bersama Anda.
`.trim();
}

function buildFaq(svc, city) {
  const c = city.name;
  const short = svc.short;
  return [
    {
      q: `Berapa biaya ${short} di ${c}?`,
      a: 'Biaya bergantung pada ruang lingkup: jumlah halaman, tingkat custom, dan integrasi yang '
        + 'dibutuhkan. Konsultasi awal tidak dipungut biaya, dan estimasi tertulis diberikan '
        + 'sebelum pekerjaan dimulai.',
    },
    {
      q: `Berapa lama pengerjaan ${short}?`,
      a: 'Paket standar umumnya 1–3 minggu. Proyek custom atau sistem berskala besar memerlukan '
        + 'waktu lebih lama, ditentukan setelah spesifikasi disepakati.',
    },
    {
      q: `Bisakah memakai domain sendiri di ${c}?`,
      a: 'Bisa. Anda menyediakan akses domain, tim teknis kami yang menangani pengaturan, DNS, dan '
        + 'hosting. Aset tetap berada di atas nama Anda.',
    },
    {
      q: 'Apakah harga termasuk domain, hosting, dan pemeliharaan?',
      a: 'Belum. Domain dan hosting dibayar langsung kepada penyedia agar Anda memiliki kontrol '
        + 'penuh. Pemeliharaan ditawarkan sebagai paket terpisah agar tidak ada biaya tersembunyi.',
    },
    {
      q: 'Setelah website tayang, apakah bisa diubah sendiri?',
      a: 'Untuk website statis, seluruh konten dapat Anda ubah sendiri. Untuk sistem dinamis, '
        + 'dashboard dan panduan operasional disertakan saat serah terima.',
    },
    {
      q: `Bagaimana cara memulai proyek ${short} di ${c}?`,
      a: 'Kirim kebutuhan Anda melalui halaman kontak. Tim kami akan menghubungi Anda untuk '
        + 'konsultasi awal, lalu menyusun estimasi dan ruang lingkup kerja.',
    },
  ];
}

/* ------------------------------------------------------------------ */
/* Helpers                                                             */
/* ------------------------------------------------------------------ */
const esc = (s) => String(s).replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\s+/g, ' ').trim();

function siblingsFor(citySlug) {
  return CITIES.filter((c) => c.slug !== citySlug).map((oc) => ({
    url: `/jasa/${SERVICES[0].slug}-${oc.slug}/`,
    title: SERVICES[0].title(oc.name),
  }));
}

/* ------------------------------------------------------------------ */
/* Tulis semua artikel                                                 */
/* ------------------------------------------------------------------ */
fs.mkdirSync(OUT_DIR, { recursive: true });
for (const f of fs.readdirSync(OUT_DIR)) {
  if (f.endsWith('.md')) fs.unlinkSync(path.join(OUT_DIR, f));
}

let count = 0;

for (const city of CITIES) {
  const siblings = siblingsFor(city.slug);

  for (const svc of SERVICES) {
    const slug = `${svc.slug}-${city.slug}`;
    const faq = buildFaq(svc, city);
    const title = svc.title(city.name);
    const description = svc.desc(city.name);
    const h1 = svc.h1(city.name);

    const front = [
      '---',
      'layout: seo-article',
      `title: "${esc(title)}"`,
      `description: "${esc(description)}"`,
      `city: "${esc(city.name)}"`,
      `province: "${esc(city.province)}"`,
      `service_label: "${esc(svc.label)}"`,
      `service_short: "${esc(svc.short)}"`,
      `cta_text: "${esc(svc.ctaText)}"`,
      `cta_url: "${svc.ctaUrl}"`,
      `permalink: /jasa/${slug}/`,
      `primary_keyword: "${esc(svc.slug.replace(/-/g, ' ') + ' ' + city.slug)}"`,
      'siblings:',
      ...siblings.map((s) => `  - url: "${s.url}"\n    title: "${esc(s.title)}"`),
      'related_services:',
      ...RELATED.map((r) => `  - title: "${esc(r.title)}"\n    url: "${r.url}"`),
      'faq:',
      ...faq.map((f) => `  - q: "${esc(f.q)}"\n    a: "${esc(f.a)}"`),
      '---',
      '',
    ].join('\n');

    const body = [
      front,
      buildBody(svc, city),
      '',
      '## Langkah berikutnya',
      '',
      `Siap mulai ${svc.short} di ${city.name}? Sampaikan kebutuhan Anda lewat `
      + `[halaman kontak](/kontak/) atau hubungi WhatsApp ${BRAND_PHONE}. `
      + 'Konsultasi awal tidak dipungut biaya.',
      '',
    ].join('\n');

    fs.writeFileSync(path.join(OUT_DIR, `${slug}.md`), body);
    count++;
  }
}

console.log(`Generated ${count} SEO articles (${SERVICES.length} keyword x ${CITIES.length} kota).`);
console.log(`Bali regions available as follow-up targets: ${BALI_REGIONS.map((b) => b.name).join(', ')}`);
console.log(`Output directory: ${OUT_DIR}`);