---
layout: page
title: Kebijakan Privasi Bimbel Offline
description: "Privasi aplikasi Bimbel Offline: data lokal di SQLite, PIN 4 digit, tanpa izin INTERNET, iklan, atau analitik."
eyebrow: Privasi
permalink: /privacy-policy-bimbel-offline/
og_image: '/assets/img/og/tentang-og.jpg'
---

Berlaku sejak: 26 November 2026

Aksisoft Media menghormati privasi pengguna aplikasi **Bimbel Offline** (`id.aksisoft.bimbelhub`). Halaman ini menjelaskan secara ringkas dan lengkap bagaimana aplikasi menangani data Anda. Kebijakan privasi umum kami tersedia di [aksisoft.web.id/privacy-policy](/privacy-policy/).

## Ringkasan

- Bimbel Offline adalah aplikasi **offline-first** yang bekerja **tanpa koneksi internet**. Aplikasi **tidak meminta izin `INTERNET`**.
- Kami **tidak memiliki server penyimpanan data**, **tidak ada akun pengguna**, dan **tidak ada login daring**.
- Seluruh data — siswa, guru, program, jadwal dan sesi, absensi, pendaftaran, tagihan, pembayaran, pengeluaran, honor guru, serta pengaturan — disimpan **hanya di perangkat Anda**, di dalam database lokal SQLite (`bimbel_offline.sqlite`).
- Aplikasi dibuka dengan **PIN 4 digit** yang Anda atur sendiri di perangkat.
- **Tidak ada** pengumpulan atau pengiriman data pribadi ke pihak ketiga. **Tidak ada iklan pihak ketiga** dan **tidak ada analitik**.
- **Backup dan restore** dilakukan sendiri oleh Anda secara lokal menggunakan berkas JSON. Kami tidak pernah menerima salinannya.

## Data yang disimpan di perangkat Anda

Aplikasi menyimpan data yang Anda masukkan agar Anda dapat mengelola bimbingan belajar tanpa internet:

- **Siswa dan wali:** nama, nama wali, nomor WhatsApp, alamat, sekolah, kelas, dan catatan.
- **Guru:** nama, nomor telepon/WhatsApp, mata pelajaran, tarif per sesi, dan status.
- **Program, jadwal, dan absensi:** program belajar, pendaftaran siswa, jadwal pertemuan, sesi, serta catatan kehadiran.
- **Keuangan:** tagihan, pembayaran, pengeluaran, dan honor guru.
- **Pengaturan:** nama dan alamat bimbel, nomor WhatsApp untuk pesan otomatis, serta PIN aplikasi.

Semua data tersebut berada di penyimpanan aplikasi pada perangkat Anda. Kami tidak mengunggahnya, tidak menyimpannya di server kami, dan tidak membuat salinan di luar perangkat Anda.

## Izin aplikasi

Aplikasi **tidak meminta izin `INTERNET`**, sehingga tidak dapat mengirim data ke jaringan dari dalam aplikasi. Aplikasi juga tidak meminta izin lokasi, kontak, kamera, mikrofon, atau SMS untuk mengumpulkan data.

| Izin / akses | Status dan tujuan |
|---|---|
| `android.permission.INTERNET` | **Tidak diminta.** Aplikasi berjalan penuh offline. |
| Pemilih berkas sistem | Hanya digunakan saat Anda sendiri memilih berkas JSON untuk **restore** data. |
| Berbagi berkas sistem | Hanya digunakan saat Anda sendiri menekan **Backup** untuk membagikan berkas cadangan. |
| WhatsApp (melalui `url_launcher`) | Hanya membuka aplikasi WhatsApp ketika Anda sengaja menekan tombol WhatsApp. |

## Tidak ada server, akun, iklan, atau analitik

- **Tanpa akun daring:** tidak ada pendaftaran, email, kata sandi, atau login online.
- **Tanpa server:** tidak ada backend yang menerima, menyimpan, atau memproses data Anda.
- **Tanpa iklan:** tidak ada jaringan iklan pihak ketiga, tidak ada ID iklan, dan tidak ada penargetan iklan.
- **Tanpa analitik:** tidak ada pelacakan pengguna, pengukuran aktivitas, atau pelaporan kerusakan yang mengirim data keluar dari perangkat.

## WhatsApp dan tautan eksternal

Pada layar jadwal dan tagihan tersedia tombol WhatsApp untuk menghubungi guru atau wali siswa. Tombol ini memakai `url_launcher` dengan mode aplikasi eksternal dan **hanya berjalan jika Anda sengaja menekannya**. Aplikasi tidak mengirim pesan otomatis, tidak membaca daftar kontak Anda, tidak mengakses riwayat percakapan, dan tidak menerima isi pesan tersebut. Jika WhatsApp tidak terpasang, tidak ada data yang dikirim.

## Cadangan dan pemulihan data

Melalui menu **Pengaturan**, Anda dapat:

- **Backup Database** — mengekspor seluruh tabel aplikasi menjadi satu berkas JSON (`bimbel-offline-backup-<waktu>.json`) lalu membagikannya melalui aplikasi pilihan Anda.
- **Restore Database** — memilih berkas JSON cadangan dari perangkat Anda; data saat ini akan ditimpa setelah Anda mengonfirmasi.

Berkas cadangan dibuat dan dibaca **di perangkat Anda**. Isinya dapat mencakup data siswa, guru, dan keuangan, jadi simpanlah di tempat yang Anda percaya. Kami tidak menyediakan cadangan cloud dan tidak memiliki akses ke berkas tersebut.

## Keamanan dan PIN

Saat membuka aplikasi, Anda diminta memasukkan **PIN 4 digit** yang Anda atur sendiri melalui menu **Pengaturan**. PIN ini disimpan di perangkat Anda dan berfungsi sebagai pengunci akses ke aplikasi. Kami tidak mengetahui PIN Anda, tidak mengirimkannya ke mana pun, dan tidak dapat memulihkannya untuk Anda. Gunakan PIN yang tidak mudah ditebak dan jangan bagikan kepada orang lain.

## Hak Anda

Karena semua data berada di perangkat Anda, Anda memiliki kendali penuh atas data tersebut. Anda dapat:

- melihat, mengubah, atau menghapus data siswa, guru, jadwal, absensi, dan catatan keuangan langsung di aplikasi;
- mengekspor salinan data Anda kapan saja lewat **Backup Database**;
- memulihkan data dari berkas cadangan yang Anda simpan sendiri;
- menghubungi kami untuk pertanyaan mengenai kebijakan ini melalui kontak di bawah.

## Retensi dan penghapusan data

Data disimpan di perangkat Anda selama Anda membutuhkannya; kami tidak menentukan masa retensi karena kami tidak menyimpan data Anda. Untuk menghapusnya:

- gunakan **Hapus data contoh** di menu Pengaturan untuk menghapus data bawaan/contoh beserta data yang Anda input; atau
- hapus data aplikasi melalui **Setelan Android → Aplikasi → Bimbel Offline → Hapus data**, atau **uninstall** aplikasi untuk menghapus seluruh data termasuk database `bimbel_offline.sqlite` dan PIN.

Menghapus instalasi aplikasi bersifat permanen. Kami sangat menyarankan membuat cadangan JSON terlebih dahulu jika Anda ingin menyimpan data.

Perlu dicatat: karena aplikasi tidak memiliki akun atau server, kami **tidak dapat memulihkan** data yang sudah dihapus dari perangkat Anda.

## Anak-anak

Aplikasi ini ditujukan untuk pengelola bimbingan belajar (orang dewasa) dan tidak dirancang untuk anak-anak. Kami tidak mengumpulkan data pribadi dari siapa pun, termasuk anak-anak.

## Perubahan kebijakan

Jika kebijakan ini berubah, versi terbaru akan dipublikasikan pada halaman ini beserta tanggal berlakunya.

## Kontak

Pertanyaan tentang kebijakan privasi ini dapat disampaikan kepada:

- **Developer:** Aksisoft Media
- **Email:** aksisoftsby@gmail.com
- **WhatsApp:** +62 813-3520-6389
- **Situs:** [aksisoft.web.id](https://aksisoft.web.id/)
