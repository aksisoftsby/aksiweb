Anda bertindak sebagai senior UI/UX designer sekaligus developer Jekyll yang bertugas melakukan redesign menyeluruh pada website **aksisoft.web.id** yang saat ini menggunakan **Jekyll** dan dikelola melalui **GitHub**.

## TUJUAN UTAMA

Redesign website agar memiliki tampilan modern, profesional, premium, bersih, dan konsisten seperti konsep desain referensi yang diberikan.

Gunakan karakter visual utama:

* Warna utama: **burgundy / merah tua**
* Warna pendukung: putih, off-white, abu-abu sangat muda
* Sedikit aksen merah terang bila diperlukan
* Tampilan modern dan profesional
* Banyak whitespace
* Card dengan sudut membulat
* Border halus
* Shadow sangat lembut
* Typography modern, jelas, dan mudah dibaca
* Visual produk / website / aplikasi yang kuat
* Layout responsive
* Desktop dan mobile harus sama-sama diperhatikan
* Hindari desain yang terlalu ramai
* Hindari efek berlebihan
* Gunakan animasi ringan hanya apabila benar-benar membantu UX

Konsep visual harus terasa seperti:

**IDEA · BUILD · SOLUTION**

Website harus memberikan kesan bahwa Aksisoft adalah perusahaan/brand teknologi yang profesional dan mampu membuat website, aplikasi, sistem, serta solusi digital.

---

# ATURAN PALING PENTING

### 1. JANGAN MENGUBAH MENU YANG SUDAH ADA

Sebelum melakukan perubahan apa pun, **scan seluruh repository Jekyll**.

Cari dan identifikasi:

* menu navbar
* menu mobile
* dropdown
* submenu
* footer navigation
* link internal
* kategori
* tag
* halaman
* collection
* permalink
* route
* URL penting

**Jangan menghapus menu yang sudah ada.**

**Jangan mengganti nama menu.**

**Jangan mengubah struktur navigasi tanpa alasan yang sangat kuat.**

**Jangan membuat menu baru hanya demi mengikuti desain referensi.**

Desain boleh berubah secara visual, tetapi **informasi architecture dan menu existing harus tetap dipertahankan**.

---

# 2. AUDIT SELURUH HALAMAN SATU PER SATU

Jangan hanya mengubah homepage.

Buka dan periksa seluruh halaman yang terdapat di repository.

Identifikasi minimal:

* Homepage
* halaman layanan
* halaman portofolio
* halaman tentang
* halaman kontak
* halaman blog
* halaman artikel
* halaman kategori
* halaman tag
* halaman proyek
* halaman legal
* halaman lain yang ditemukan di repository

Untuk setiap halaman:

1. Baca isi kontennya.
2. Identifikasi layout existing.
3. Identifikasi template/layout Jekyll yang digunakan.
4. Identifikasi komponen yang digunakan bersama halaman lain.
5. Cek apakah halaman tersebut cocok dengan visual baru.
6. Tentukan apakah cukup melakukan perubahan style.
7. Tentukan apakah perlu perubahan struktur layout.
8. Pastikan fungsi dan konten penting tidak hilang.

Buat pemetaan internal:

```text
URL / Page
↓
Layout Jekyll
↓
Komponen
↓
Tujuan halaman
↓
Masalah desain saat ini
↓
Solusi redesign
```

Jangan menerapkan satu layout secara paksa ke semua halaman.

---

# 3. JANGAN MEMBUAT SEMUA HALAMAN 100% SAMA

Homepage boleh menjadi visual utama.

Halaman lain **tidak harus memiliki struktur identik** dengan homepage.

Namun seluruh website harus terasa berasal dari satu design system.

Contohnya:

Homepage:

* Hero besar
* layanan
* statistik
* portofolio
* keunggulan
* testimonial
* CTA
* footer

Halaman layanan:

* Page header
* deskripsi layanan
* manfaat
* proses kerja
* fitur
* FAQ
* CTA

Halaman portofolio:

* Page header
* filter/kategori
* grid proyek
* detail proyek
* gallery
* CTA

Halaman artikel:

* typography yang lebih nyaman dibaca
* metadata
* featured image
* content body
* related articles
* CTA

Jadi **layout menyesuaikan fungsi halaman**, tetapi warna, typography, spacing, card, button, border-radius, icon style, dan elemen visual tetap konsisten.

---

# 4. GUNAKAN DESIGN SYSTEM

Bangun design system yang reusable.

Tentukan variable CSS untuk:

```css
--color-primary
--color-primary-dark
--color-primary-light
--color-background
--color-surface
--color-text
--color-text-muted
--color-border
--color-success
--color-danger

--radius-sm
--radius-md
--radius-lg
--radius-xl

--shadow-sm
--shadow-md
--shadow-lg

--container-width

--spacing-xs
--spacing-sm
--spacing-md
--spacing-lg
--spacing-xl
--spacing-2xl
```

Jangan membuat warna berbeda-beda secara manual di setiap halaman.

Seluruh website harus menggunakan variable/design token yang sama.

---

# 5. WARNA

Pertahankan identitas **burgundy / merah tua** sebagai warna utama.

Gunakan burgundy secara elegan, bukan memenuhi seluruh layar.

Gunakan misalnya:

* burgundy untuk CTA utama
* burgundy untuk heading emphasis
* burgundy untuk icon
* burgundy untuk link aktif
* burgundy section tertentu
* burgundy gradient secara terbatas

Background utama:

* putih
* off-white
* sangat sedikit pinkish-white bila diperlukan

Hindari:

* warna biru sebagai warna utama
* gradient warna-warni berlebihan
* neon
* terlalu banyak warna aksen

---

# 6. HOMEPAGE

Homepage harus menjadi representasi utama desain baru.

Struktur visual dapat dikembangkan seperti:

### Header

Logo Aksisoft.

Navbar menggunakan menu yang **sudah ada saat ini**.

Desktop:

```text
Logo | Menu 1 | Menu 2 | Menu 3 | Menu 4 | Menu 5 | CTA
```

Mobile:

* hamburger
* existing menu tetap tersedia

Gunakan header yang modern, bersih, dan sedikit elevated.

---

### Hero

Buat hero yang kuat.

Gunakan headline besar seperti konsep:

**Wujudkan Ide Anda Menjadi Solusi Nyata**

atau gunakan headline existing apabila sudah lebih sesuai dengan brand.

Subheadline menjelaskan bahwa Aksisoft menyediakan solusi digital untuk bisnis, organisasi, komunitas, dan individu.

CTA utama:

**Mulai Sekarang**

CTA kedua:

**Lihat Portofolio**

Gunakan visual:

* laptop
* smartphone
* mockup website
* dashboard
* aplikasi

Visual boleh menggunakan asset existing repository apabila tersedia.

Jangan mengganti image dengan placeholder apabila asset asli tersedia.

---

### Layanan

Gunakan card modern.

Contoh kategori:

* Website Profesional
* Aplikasi Mobile
* Sistem Custom
* Optimasi & SEO

Tetapi **jangan menambah atau menghilangkan layanan existing hanya berdasarkan contoh tersebut**.

Sesuaikan dengan layanan aktual yang ditemukan di repository.

---

### Statistik / Trust

Apabila website memiliki data nyata, tampilkan secara visual.

Contoh:

* proyek
* klien
* pengalaman
* layanan

**Jangan mengarang angka.**

Jika tidak ada data nyata, jangan membuat statistik palsu.

---

### Portfolio

Tampilkan proyek yang benar-benar ada di website.

Gunakan:

* thumbnail
* nama proyek
* kategori
* deskripsi singkat

Buat grid modern.

Gunakan image existing.

Optimalkan gambar agar tidak memperlambat website.

---

### Why Aksisoft

Buat section yang menjelaskan value proposition.

Contoh:

* pengalaman
* kualitas
* dukungan
* solusi sesuai kebutuhan
* harga kompetitif

Tetapi gunakan informasi aktual dari website.

---

### CTA

Buat CTA section yang jelas.

Contoh konsep:

**Konsultasikan Ide Anda Sekarang**

Gunakan burgundy sebagai warna dominan section CTA.

---

### Footer

Footer harus mempertahankan semua informasi existing:

* menu
* link
* copyright
* social media
* kontak
* informasi lain yang memang sudah tersedia

Jangan menghapus informasi existing hanya karena tidak ada di mockup.

---

# 7. TYPOGRAPHY

Gunakan typography modern dan profesional.

Prioritaskan:

* readability
* hierarchy
* heading yang kuat
* body text nyaman dibaca

Hindari terlalu banyak font.

Ideal:

```text
1 font family utama
2–3 weight utama
```

Pastikan:

* H1 kuat
* H2 jelas
* H3 proporsional
* body text nyaman
* metadata lebih kecil
* button jelas

Untuk artikel/blog, prioritaskan readability daripada tampilan marketing.

---

# 8. COMPONENT SYSTEM

Buat komponen reusable Jekyll.

Contoh:

```text
_includes/
    header.html
    navbar.html
    mobile-menu.html
    footer.html
    hero.html
    section-heading.html
    service-card.html
    portfolio-card.html
    testimonial-card.html
    cta.html
```

Gunakan component yang sama di banyak halaman bila memang sesuai.

Jangan menduplikasi HTML yang sama di puluhan file.

---

# 9. LAYOUT SYSTEM JEKYLL

Audit `_layouts`.

Pertahankan layout existing yang masih berguna.

Refactor jika diperlukan.

Contoh:

```text
_layouts/
    default.html
    page.html
    post.html
    portfolio.html
```

Buat layout khusus hanya jika memang dibutuhkan.

Jangan menghancurkan struktur Jekyll existing hanya untuk mendapatkan tampilan baru.

---

# 10. RESPONSIVE

Website harus benar-benar responsive.

Test minimal:

```text
320px
375px
390px
414px
768px
1024px
1280px
1440px
1920px
```

Mobile bukan sekadar desktop yang dikecilkan.

Perhatikan:

* navbar
* typography
* button
* card
* grid
* image
* spacing
* hero
* footer
* tabel jika ada
* article readability

Tidak boleh:

* horizontal overflow
* text terpotong
* gambar keluar container
* button terlalu kecil
* menu sulit disentuh

---

# 11. SEO

Jangan merusak SEO existing.

Pertahankan:

* title
* meta description
* canonical
* Open Graph
* Twitter/X card
* structured data jika ada
* sitemap
* robots
* permalink

Audit apakah terdapat SEO configuration existing.

Jangan mengubah URL existing tanpa alasan yang valid.

Jika URL harus berubah, pertimbangkan redirect.

---

# 12. PERFORMANCE

Jangan membuat desain bagus tetapi website menjadi berat.

Optimalkan:

* image
* CSS
* JavaScript
* font
* lazy loading
* responsive image
* asset loading

Gunakan JavaScript sesedikit mungkin.

Untuk animasi:

* CSS terlebih dahulu
* JS hanya jika benar-benar diperlukan

Jangan memasukkan framework besar seperti React/Vue hanya untuk redesign ini.

Website tetap menggunakan **Jekyll**.

---

# 13. GITHUB

Website tetap kompatibel dengan:

**GitHub Pages / GitHub repository workflow yang sekarang digunakan.**

Sebelum melakukan perubahan:

* cek `_config.yml`
* cek `Gemfile`
* cek plugin
* cek GitHub Actions
* cek build configuration
* cek deployment configuration

Jangan menghapus konfigurasi GitHub yang masih diperlukan.

Pastikan setelah redesign:

```text
bundle exec jekyll build
```

berhasil.

Jika repository memiliki workflow build/deploy, pastikan workflow tetap valid.

---

# 14. JANGAN MENGHILANGKAN FITUR

Seluruh fitur existing harus tetap bekerja.

Audit:

* search
* pagination
* category
* tags
* sharing
* contact form
* navigation
* dropdown
* breadcrumbs
* gallery
* filter
* external link
* internal link
* mobile navigation
* script existing

Redesign visual **tidak boleh mengorbankan functionality**.

---

# 15. BAHASA

**Gunakan bahasa Indonesia untuk seluruh UI website.**

Jangan mengganti copy menjadi bahasa Inggris.

Jangan menerjemahkan menu existing ke bahasa lain.

Pertahankan wording existing apabila masih baik.

Copy baru hanya dibuat jika diperlukan untuk mengisi struktur desain baru.

Semua:

* heading
* button
* label
* navigation
* section
* form
* error message
* CTA

harus tetap menggunakan **bahasa Indonesia**.

---

# 16. GAMBAR DAN ASSET

Sebelum membuat asset baru:

1. Cari asset existing.
2. Gunakan asset existing jika relevan.
3. Jangan mengganti logo.
4. Jangan mengganti identitas brand.
5. Jangan menggunakan image placeholder jika asset asli tersedia.

Jika dibutuhkan visual baru, gunakan style yang konsisten:

* modern
* clean
* profesional
* teknologi
* burgundy
* putih
* premium

---

# 17. JANGAN ASAL MENGUBAH CONTENT

Konten existing harus dianggap sebagai sumber utama.

Jangan menghapus paragraph, informasi layanan, portfolio, metadata, atau detail lain hanya karena ingin membuat tampilan minimalis.

Tugas utama adalah:

**REDESIGN UI/UX, bukan menghapus isi website.**

Apabila konten terlalu panjang untuk layout tertentu:

* rapikan hierarchy
* gunakan accordion
* gunakan card
* gunakan tabs jika cocok
* gunakan section
* gunakan pagination

Jangan menghapus informasi penting.

---

# 18. AUDIT SEBELUM CODING

Sebelum melakukan perubahan kode, lakukan audit repository.

Buat catatan internal mengenai:

```text
1. Struktur repository
2. Semua layout
3. Semua include
4. Semua halaman
5. Semua collection
6. Semua menu
7. Semua URL
8. Semua asset
9. Semua CSS
10. Semua JavaScript
11. Konfigurasi Jekyll
12. Konfigurasi GitHub
```

Kemudian mapping halaman:

```text
Homepage → redesign penuh
Services → redesign sesuai fungsi
Portfolio → redesign sesuai fungsi
Post → redesign article
Static Page → redesign page
Legal → redesign minimal
```

---

# 19. PRIORITAS DESAIN

Gunakan urutan prioritas:

```text
Usability
↓
Readability
↓
Consistency
↓
Visual hierarchy
↓
Branding
↓
Animation
```

Jangan mengejar efek visual sampai mengorbankan usability.

---

# 20. HASIL AKHIR YANG DIHARAPKAN

Setelah selesai, website harus terasa seperti **satu brand yang utuh**.

Ketika user berpindah:

```text
Homepage
→ Layanan
→ Portfolio
→ Detail Portfolio
→ Tentang
→ Artikel
→ Kontak
```

mereka harus langsung merasa masih berada di website yang sama.

Bukan setiap halaman mempunyai desain sendiri-sendiri.

Namun jangan pula membuat semua halaman identik.

Gunakan:

**satu design system + banyak layout yang sesuai fungsi halaman.**

---

# 21. VALIDASI AKHIR

Sebelum menyatakan selesai, lakukan pemeriksaan:

### Navigation

* semua menu existing masih ada
* semua link berfungsi
* mobile menu berfungsi

### Jekyll

* build berhasil
* tidak ada Liquid error
* tidak ada broken include
* tidak ada broken layout

### Visual

* warna burgundy konsisten
* typography konsisten
* spacing konsisten
* card konsisten
* button konsisten

### Responsive

* mobile
* tablet
* desktop
* ultra-wide

### Content

* tidak ada informasi penting yang hilang
* tidak ada konten palsu
* tidak ada angka/statistik hasil karangan

### SEO

* title
* description
* canonical
* metadata
* sitemap
* permalink

### Performance

* image optimized
* JS minimal
* CSS efisien
* tidak ada dependency tidak perlu

---

# 22. ATURAN IMPLEMENTASI

Kerjakan secara bertahap:

### Tahap 1

Audit seluruh repository.

### Tahap 2

Audit semua halaman satu per satu.

### Tahap 3

Buat design system.

### Tahap 4

Redesign global:

* typography
* colors
* spacing
* buttons
* cards
* navbar
* footer

### Tahap 5

Redesign homepage.

### Tahap 6

Redesign halaman lain sesuai fungsi masing-masing.

### Tahap 7

Responsive optimization.

### Tahap 8

SEO + performance audit.

### Tahap 9

Build dan validasi Jekyll.

### Tahap 10

Final review seluruh halaman.

---

# INSTRUKSI TERAKHIR

**Jangan langsung coding setelah melihat homepage.**

Baca repository terlebih dahulu.

**Cek satu per satu halaman yang ada.**

Tentukan sendiri apakah setiap halaman:

* sudah cocok dengan design system baru,
* perlu redesign ringan,
* perlu redesign struktural,
* atau cukup menggunakan styling baru.

Gunakan keputusan desain yang masuk akal berdasarkan **fungsi masing-masing halaman**.

Referensi visual utama adalah desain landing page Aksisoft dengan nuansa **burgundy / merah tua + putih**, tetapi halaman lain **tidak harus 100% identik**.

Jangan mengubah menu existing.

Jangan mengubah bahasa website ke bahasa lain.

Jangan menghapus konten penting.

Jangan mengarang data.

Jangan mengganti Jekyll dengan framework lain.

Jangan menambahkan framework frontend besar yang tidak diperlukan.

Hasil akhirnya harus terlihat seperti **versi baru Aksisoft yang modern, profesional, premium, konsisten, cepat, responsive, dan tetap kompatibel dengan workflow Jekyll + GitHub yang sekarang.**
