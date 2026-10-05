# Deploy ke aksisoft.web.id tanpa build Jekyll di GitHub

Build Jekyll GitHub Actions sudah tidak bisa dipakai (kuota/limit), jadi
situs sekarang **dibangun secara lokal** dan hasilnya di-push sebagai
output statis.

## Struktur branch

| Branch | Isi |
|---|---|
| `source` | Source Jekyll (tempat kamu mengedit konten) |
| `gh-pages` | **Output** build (`_site`) + `.nojekyll` |

`.nojekyll` membuat GitHub Pages menyajikan file apa adanya — build
Actions dilewati sepenuhnya, jadi kuota Actions tidak terpakai dan
deploy hanya butuh ±40 detik.

## Cara deploy (setelah edit konten)

```bash
bash deploy-pages.sh
```

Skrip ini: build Jekyll lokal → bersihkan `_site` → commit output ke
`gh-pages` → push. Tunggu ±1 menit, situs live.

## Ruby portable

Build memakai Ruby 3.3.12 + Jekyll 4.4.1 yang terpasang di
`F:/repo/.rubyportable/` (di luar repo, tidak ikut ter-commit).

Kalau hilang/berpindah komputer, pasang ulang:

```bash
# 1. Download rubyinstaller-3.3.12-1-x64.7z dari
#    https://github.com/oneclick/rubyinstaller2/releases
# 2. Ekstrak ke F:/repo/.rubyportable/ (mis. dengan py7zr: pip install py7zr)
# 3. Pasang gem:
export GEM_HOME=F:/repo/.rubyportable/rubyinstaller-3.3.12-1-x64/lib/ruby/gems/3.3.0
F:/repo/.rubyportable/rubyinstaller-3.3.12-1-x64/bin/gem.cmd install --no-document \
  jekyll jekyll-seo-tag jekyll-sitemap jekyll-feed pathutil rouge safe_yaml \
  terminal-table webrick addressable colorator unicode-display_width \
  public_suffix i18n ffi sass-embedded listen jekyll-sass-converter \
  kramdown kramdown-parser-gfm liquid mercenary rexml tzinfo tzinfo-data \
  em-websocket --ignore-dependencies
# 4. eventmachine & http_parser.rb tidak terpasang (perlu MSYS2); pakai stub:
#    buat gemspec kosong lalu `gem build` + `gem install --local`
#    (dipakai hanya agar aktivasi jekyll lolos; `jekyll build` tidak memakainya)
```

## Catatan

- **File video tidak pernah masuk repo lagi** (lihat `.gitignore`):
  semuanya di `cfcdn.aksisoft.my.id`, URL terdaftar di `_data/videos.json`.
- Lupa push `source`? Konten tetap aman — `gh-pages` yang menentukan situs.
- Backup history lama (sebelum rewrite): `F:\repo\aksiweb-backup-*.bundle`.
