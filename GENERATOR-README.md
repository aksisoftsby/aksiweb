# GENERATOR-README.md

Generator otomatis: **API → static Jekyll files**. Semua data (katalog & detail page) di-hardcode ke file Jekyll saat generate. Tidak ada fetch API di browser/runtime — website tetap berfungsi walau API offline.

## Requirement

- **Node.js** (wajib) — https://nodejs.org (versi 18+, built-in `fetch`)
- **Jekyll / Ruby / Bundler** (opsional, hanya untuk `jekyll build`)

## Cara menjalankan

```bat
generate.bat
```

Proses otomatis: fetch listing API → validasi → normalize data → fetch detail tiap website (concurrency 5, dengan fallback endpoint) → generate `_data/websites.json` → generate halaman detail `_websites/{slug}.md` → validasi → summary.

## Flag

| Command | Fungsi |
|---|---|
| `generate.bat` | Generate normal (tidak pernah menghapus file) |
| `generate.bat --debug` | Tampilkan detail: API URL, HTTP status, detail URL, image count, dll. |
| `generate.bat --clean` | Hapus `_websites/{slug}.md` yang slug-nya tidak ada lagi di API |
| `generate.bat --build` | Jalankan `bundle exec jekyll build` setelah generate |

## Konfigurasi

Semua konfigurasi ada di bagian `CONFIG` paling atas `generate.js`:

| Key | Default | Keterangan |
|---|---|---|
| `listingApi` | `https://template.aksisoft.web.id/api/websites` | Endpoint listing |
| `detailApiBySlug` | `.../api/websites/slug/` | Endpoint detail (prioritas) |
| `detailApiFallback` | `.../api/v1/websites/` | Endpoint detail fallback (slug lalu id) |
| `imageBaseUrl` | `https://template.aksisoft.web.id` | Prefix untuk image path relatif (`/demo/...`) |
| `dataFile` | `_data/websites.json` | Output data katalog |
| `detailDir` | `_websites` | Collection detail page (URL: `/website/{slug}/`) |
| `concurrency` | `5` | Jumlah request simultan |
| `buildAfterGenerate` | `false` | Auto jekyll build |

## Output

```text
_data/websites.json          -> data katalog (dipakai _layouts/catalog.html)
_websites/{slug}.md          -> halaman detail statis per template (layout: website)
pages/website.html           -> halaman katalog /website/ (statis, loop site.websites)
```

## Halaman

- Katalog: `/website/`
- Detail: `/website/{slug}/` contoh `/website/vibranted-school/`

## Idempotent

Script bisa dijalankan berulang kali — file yang sama di-update, tidak ada duplikat. Duplicate slug di API dideteksi dan dilewati dengan warning. Kegagalan fetch detail satu item tidak menghentikan proses (fallback ke data listing).
