# Website Jasa Pembuatan Website - GitHub Pages

Template website statis berbasis Jekyll untuk GitHub Pages. Cocok untuk jasa pembuatan website, company profile, landing page, dan blog.

## Fitur

- Beranda, Layanan, Blog, Tentang, Kontak
- Blog dengan folder `_posts`
- SEO memakai `jekyll-seo-tag`
- Sitemap otomatis memakai `jekyll-sitemap`
- RSS/Atom feed memakai `jekyll-feed`
- Workflow GitHub Actions untuk deploy GitHub Pages
- Responsive design

## Cara pakai cepat

1. Buat repository baru di GitHub.
2. Upload semua file template ini ke repository.
3. Edit `_config.yml`:
   - Ganti `USERNAME` dengan username GitHub Anda.
   - Ganti `REPOSITORY` dengan nama repository.
   - Edit `title`, `description`, `author`, dan kontak.
4. Di GitHub buka **Settings → Pages**.
5. Pada **Build and deployment**, pilih **GitHub Actions**.
6. Push ke branch `main`.

## Custom domain .com

Tambahkan file bernama `CNAME` di root repository, isi dengan domain Anda, contoh:

```txt
www.domainanda.com
```

Lalu arahkan DNS domain ke GitHub Pages sesuai instruksi GitHub.

## Plugin yang dipakai

Plugin dipilih yang kompatibel dengan GitHub Pages:

```yml
plugins:
  - jekyll-seo-tag
  - jekyll-sitemap
  - jekyll-feed
```

