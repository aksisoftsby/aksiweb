---
layout: portfolio
title: EventMedia.id — Katalog Event & Direktori
description: "Katalog event dan direktori vendor EventMedia.id: katalog per kategori & kota, pengajuan event dengan moderasi, direktori berbayar, dan API publik."
category: Katalog & Direktori
image: /assets/img/portfolio/eventmedia.webp
site_url: https://eventmedia.my.id/
site_label: eventmedia.my.id
gallery:
  - /assets/img/portfolio/eventmedia-event.webp
  - /assets/img/portfolio/eventmedia-direktori.webp
  - /assets/img/portfolio/eventmedia-artikel.webp
  - /assets/img/portfolio/eventmedia-kota.webp
order: 8
og_image: '/assets/img/og/portfolio-eventmedia.jpg'
---

## Tentang Proyek

EventMedia.id adalah platform katalog event dan direktori vendor untuk penyelenggara maupun penonton di Indonesia. Situsnya berjalan di `eventmedia.my.id` dengan merek EventMedia.id. Ada dua sisi yang dilayani sekaligus: pengunjung mencari konser, seminar, workshop, atau festival berdasarkan kategori dan kota; sementara pemilik venue, kafe, hotel, rental sound system, dan event organizer mendaftarkan usahanya ke direktori agar ditemukan panitia acara.

Semua event yang dikirim publik tidak langsung tayang. Pengajuan masuk antrean moderasi, diperiksa admin, baru kemudian dipublikasikan — supaya katalog tidak dipenuhi acara palsu atau duplikat. Data yang tampil di halaman publik dilayani lewat API JSON yang dokumentasinya terbuka, sehingga platform ini bisa dipakai ulang oleh aplikasi atau integrasi lain.

## Fitur yang Jalan

- **Katalog event** dengan pencarian nama event/venue, filter kota dan kategori, serta pemisahan format Semua, Offline, dan Online
- **8 kategori** (konser, seminar, workshop, festival, talkshow, kompetisi, pameran, komunitas) dan **8 halaman kota** dengan gambar destinasi
- **Halaman detail event**: tanggal pelaksanaan, venue, kota, penyelenggara, dan tombol akses tiket yang mengarah ke penyelenggara
- **Formulir Kirim Event** untuk publik, lengkap dengan unggah poster; masuk moderasi admin sebelum tayang
- **Direktori tempat & vendor** — hotel dan penginapan, restoran/kafe, venue gedung, rental sound system, hingga event organizer — dengan pencarian dan filter kota
- **Pendaftaran direktori berbayar** Rp 20.000 sekali bayar untuk seumur hidup, tanpa potongan komisi per transaksi
- **Artikel & inspirasi** bertema tips, insight, dan panduan memilih event
- **Login Google** untuk pengguna, plus panel admin terpisah untuk moderasi event dan pengelolaan direktori
- **API publik terdokumentasi** (OpenAPI 3.0.3, 25 endpoint): event, kategori, kota, tag, berita, direktori, statistik, unggah media, sampai autentikasi admin
- **Mode gelap**, tata letak responsif, dan metadata sosial pada setiap halaman

## Hasil & Angka

<div class="metrics-grid">
  <div class="metric-item">
    <strong>39 URL terindeks</strong>
    <p>Event, kategori, kota, direktori, dan artikel dalam sitemap</p>
  </div>
  <div class="metric-item">
    <strong>25 endpoint API</strong>
    <p>Publik dan admin, terdokumentasi dalam spesifikasi OpenAPI 3.0.3</p>
  </div>
  <div class="metric-item">
    <strong>8 event, 6 tayang</strong>
    <p>Sisanya menunggu moderasi — alur pengajuan berjalan nyata</p>
  </div>
  <div class="metric-item">
    <strong>8 kategori &amp; 8 kota</strong>
    <p>Struktur taksonomi siap ditambah tanpa mengubah kode</p>
  </div>
  <div class="metric-item">
    <strong>6 profil direktori</strong>
    <p>Vendor dan tempat yang sudah terdaftar di katalog</p>
  </div>
  <div class="metric-item">
    <strong>Rp 20.000 sekali bayar</strong>
    <p>Biaya pendaftaran direktori, tanpa komisi per transaksi</p>
  </div>
</div>

Angka di atas dibaca langsung dari `/api/stats` dan `sitemap.xml` saat halaman portofolio ini ditulis, bukan perkiraan. Katalognya memang masih kecil karena platform baru berjalan — yang sudah selesai adalah sistemnya: pengajuan, moderasi, direktori berbayar, dan API-nya.

## Catatan Teknis

- Front-end memakai Tailwind dan JavaScript vanilla; seluruh konten diambil dari API JSON di domain yang sama, jadi menambah event atau artikel tidak menyentuh kode tampilan
- API berjalan di belakang Cloudflare; gambar dan poster diunggah ke CDN lewat endpoint `/api/upload` dengan pemeriksaan ketersediaan file
- Panel admin menangani moderasi event (setujui/tolak) dan CRUD direktori, dengan autentikasi terpisah dari akun pengguna Google
- `robots.txt` menutup `/admin`, `/adminlogin`, dan `/api/admin/` dari perayapan mesin pencari
- Struktur URL bersih per jenis konten: `/event/{slug}`, `/directory/{slug}`, `/artikel/{slug}`; filter kategori dan kota memakai parameter `/event?kategori=` dan `/event?kota=`
- Dokumentasi API tersedia publik di `/apidocs`, termasuk contoh respons dan standar paginasi
