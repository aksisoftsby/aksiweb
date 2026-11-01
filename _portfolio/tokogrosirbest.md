---
layout: portfolio
title: Toko Grosir Best — Toko Online Grosir & Ritel
description: "Toko online grosir milik kami sendiri: 48 produk, bayar QRIS, cek ongkir otomatis, promo terjadwal, dan API publik."
category: Toko Online
image: /assets/img/portfolio/tokogrosirbest.webp
site_url: https://tokogrosirbest.aksisoft.web.id/
site_label: tokogrosirbest.aksisoft.web.id
gallery:
  - /assets/img/portfolio/tokogrosirbest-produk.webp
  - /assets/img/portfolio/tokogrosirbest-terlaris.webp
  - /assets/img/portfolio/tokogrosirbest-promo.webp
  - /assets/img/portfolio/tokogrosirbest-mobile.webp
order: 0
og_image: '/assets/img/og/portfolio-tokogrosirbest.jpg'
---

## Tentang Proyek

Toko Grosir Best adalah toko online yang kami jalankan sendiri — bukan sekadar demo. Isinya produk kesehatan, perawatan diri, makanan & minuman, serta kebutuhan harian dengan harga grosir, melayani pembelian satuan maupun partai besar dari gudang kami ke seluruh Indonesia.

Alasannya sederhana: kami tidak mau menjual jasa toko online dari teori. Jadi kami bangun, jalankan, dan pakai sendiri tokonya — lengkap dengan pembayaran, pengiriman, stok, dan pelanggan sungguhan. Semua yang Anda lihat di halaman ini adalah sistem yang benar-benar dipakai sehari-hari.

Toko berjalan di `tokogrosirbest.aksisoft.web.id`, halaman ringan tanpa framework berat, dan seluruh datanya (produk, kategori, promo, berita, menu, slider) diambil dari API. Artinya pemilik toko cukup mengedit data, bukan meminta programmer mengubah tampilan.

## Fitur yang Jalan

- **Katalog 48 produk** dengan pencarian, filter kategori, tag populer, dan 6 mode urutan (terlaris, termurah, diskon terbesar, terbaru, rating, harga naik/turun)
- **Keranjang + checkout** dengan alamat tujuan, ringkasan pesanan, dan status pesanan yang bisa dipantau pembeli dari halaman pembayaran
- **Bayar pakai QRIS** — satu kode QR, bisa discan dari m-banking atau e-wallet apa pun (GoPay, OVO, DANA, ShopeePay, LinkAja). Nominal mengikuti total pesanan, terverifikasi otomatis
- **Cek ongkir otomatis** lewat integrasi kurir (JNE, J&T, SiCepat, Anteraja, Ninja, Pos Indonesia, TIKI) berdasarkan berat total pesanan — ongkir ditimbang, bukan ditaksir
- **Promo terjadwal**: harga coret, badge diskon, dan hitung mundur yang berhenti sendiri saat tanggal berakhir tiba. Tidak ada promo "nyasar" yang lupa dimatikan
- **Slider hero, menu navigasi, dan halaman berita** dikontrol penuh dari data — ganti banner atau menambah artikel tidak menyentuh kode
- **Mode gelap** yang mengikuti preferensi sistem dan disimpan di perangkat pengunjung, diterapkan sebelum halaman sempat ter-render sehingga tidak ada kedip putih
- **Chat WhatsApp**, halaman tentang, FAQ, syarat ketentuan, dan kebijakan privasi siap pakai
- **Halaman affiliate** dengan 124 produk rekomendasi dan harga yang bisa disembunyikan sesuai aturan marketplace
- **API publik** (`/api/products`, `/api/categories`, `/api/promos`, `/api/news`, `/api/orders`) yang bisa dipakai aplikasi atau integrasi lain

## Hasil & Angka

<div class="metrics-grid">
  <div class="metric-item">
    <strong>48 produk tayang</strong>
    <p>4 kategori dan 16 merek, dari vitamin sampai teh herbal</p>
  </div>
  <div class="metric-item">
    <strong>Rp 8.000 &ndash; Rp 80.000</strong>
    <p>Rentang harga yang ditampilkan transparan sejak daftar</p>
  </div>
  <div class="metric-item">
    <strong>13.401 terjual</strong>
    <p>Total penghitung pesanan yang berjalan di etalase</p>
  </div>
  <div class="metric-item">
    <strong>193 URL terindeks</strong>
    <p>Produk, kategori, berita, dan halaman affiliate dalam sitemap</p>
  </div>
  <div class="metric-item">
    <strong>&plusmn; 7 KB HTML</strong>
    <p>Muat pertama tanpa framework JavaScript yang memberatkan</p>
  </div>
  <div class="metric-item">
    <strong>7 kurir &amp; QRIS</strong>
    <p>Ongkir dihitung dari berat nyata, bayar dari aplikasi apa pun</p>
  </div>
</div>

Yang terakhir itu penting: toko ini kami buat agar bisa dibuka dari ponsel murah dan sinyal desa. Tidak ada pembungkus aplikasi seberat ratusan kilobyte yang harus diunduh lebih dulu sebelum pengunjung melihat barang.

## Catatan Teknis

- Front-end JavaScript vanilla (± 60 KB logika + 44 KB halaman) dengan rendering dari data; tidak memakai React/Vue agar muat pertama tetap ringan
- Seluruh konten dinamis dilayani melalui REST API di domain yang sama, ditempatkan di belakang Cloudflare dengan cache untuk aset dan halaman cangkang
- Gambar produk, slider, dan berita dikelola lewat endpoint media; teks artikel ditulis dalam Markdown dan dirender di sisi klien
- Skema warna merah `#e81028` dengan aksen kuning `#f8c04f` — dipilih agar tombol beli dan badge promo tetap menonjol di atas latar terang maupun gelap
- SEO dasar sudah terpasang: sitemap 193 URL, metadata sosial, struktur breadcrumb, dan robots yang mengizinkan perayapan katalog
- Nama merchant QRIS terdaftar resmi atas nama Aksisoft dengan NMID pada jaringan GPN, jadi pembayaran masuk ke rekening bisnis, bukan akun pribadi

## Mau Punya Toko Seperti Ini?

Toko Grosir Best adalah bukti kami mampu mengerjakan dua sisi sekaligus: membangun sistemnya, lalu menjalankannya. Kalau Anda butuh toko online yang siap dipakai jualan hari ini — lengkap dengan QRIS, ongkir otomatis, dan katalog yang bisa Anda kelola sendiri — kami yang pasang semuanya.
