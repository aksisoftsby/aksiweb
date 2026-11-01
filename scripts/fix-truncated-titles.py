#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix-truncated-titles.py — Memasang seo_title ringkas pada halaman yang
<title>-nya terpotong otomatis oleh _includes/seo.html, supaya kata kunci
tidak hilang di hasil pencarian. H1 di halaman tetap memakai title panjang.

    python3 scripts/fix-truncated-titles.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SEOTITLE = {
    'posts/2026-05-29-cara-memilih-jasa-pembuatan-website.md': 'Panduan Memilih Jasa Pembuatan Website',
    'posts/2026-05-29-kenapa-github-pages-cocok-untuk-website-bisnis.md': 'GitHub Pages untuk Website Bisnis',
    'posts/2024-01-15-membuat-artikel-seo.md': 'Cara Menulis Artikel SEO yang Naik di Google',
    'portfolio/muslimhub-app.md': 'MuslimHub — Aplikasi Android Portal Ibadah',
    'pages/produk-ai-chat.md': 'Aksisoft AI Chat — Cerdas, Gratis, Tanpa Batas',
    'pages/produk-aksi-crm.md': 'Aksi CRM — Sistem Manajemen Pelanggan',
    'pages/produk-aksisoft-pos.md': 'AksiSoft POS — Kasir & Operasional Ritel',
    'pages/produk-muslimhub.md': 'MuslimHub — Portal Ibadah Harian Web & Android',
    'pages/produk-ridesip.md': 'RideSip — Superapp Layanan Lokal',
    'pages/produk-websekolah.md': 'WebSekolah — Profil Sekolah & PPDB Online',
}

n = 0
for rel, seo in SEOTITLE.items():
    p = os.path.join(ROOT, '_' + rel) if not rel.startswith('pages/') else os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print('  LEWAT (tidak ada):', p)
        continue
    s = open(p, encoding='utf-8').read()
    m = re.match(r'(---\n)(.*?)(\n---\n)', s, re.S)
    if not m:
        print('  LEWAT (tanpa front matter):', rel)
        continue
    fm = m.group(2)
    if re.search(r'^seo_title:', fm, re.M):
        fm2 = re.sub(r'^seo_title:\s*"?[^"\n]*"?\s*$', f'seo_title: "{seo}"', fm, count=1, flags=re.M)
    else:
        tm = re.search(r'^title:[ \t]*[^>\|&][^\n]*$', fm, re.M)
        if not tm:
            print('  LEWAT (format title tidak dikenali):', rel)
            continue
        fm2 = fm[:tm.end()] + f'\nseo_title: "{seo}"' + fm[tm.end():]
    open(p, 'w', encoding='utf-8').write(m.group(1) + fm2 + m.group(3) + s[m.end():])
    n += 1
    print(f'  {rel:58} seo_title = {seo}')
print(f'\nDiperbarui: {n} file')
