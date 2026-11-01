#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
opt-imgs.py — Kompres semua gambar situs ke WebP + resize sesuai lebar
render sebenarnya di desain (container 1200px).

Pemakaian:
    python3 scripts/opt-imgs.py           # kering (dry-run, tampilkan rencana)
    python3 scripts/opt-imgs.py --apply   # jalankan konversi + tulis ulang referensi
"""
import os, re, sys, json
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = '--apply' in sys.argv

# ---------------------------------------------------------------- mapping
# path -> (lebar target px, kualitas WebP, catatan alasan ukuran)
RULES = {
    # Hero & brand
    'assets/img/aksisoft-hero-burgundy.jpg':      (1240, 82, 'LCP beranda di .rd-browser ~620px, 2x'),
    'assets/img/aksisoft-strategy-window.jpg':    (1200, 82, 'foto halaman company profile'),
    'assets/img/aksisoft-process-window.jpg':     (1200, 82, 'tidak terpakai, tetap diringkas'),
    'assets/img/aksisoft-monogram.png':           (256,  90, 'logo header/footer 40px + PDF'),
    # Hero layanan (background CSS, container 1200)
    'assets/img/website-static-hero.jpg':         (1400, 78, 'background .service-hero'),
    'assets/img/website-news-dynamic-hero.jpg':   (1400, 78, 'background .service-hero'),
    'assets/img/aplikasi-custom-android-hero.jpg':(1400, 78, 'background .service-hero'),
    'assets/img/email-marketing-hero.jpg':        (1400, 78, 'background .service-hero'),
    'assets/img/google-ads-hero.jpg':             (1400, 78, 'background .service-hero'),
    'assets/img/social-media-ads-hero.jpg':       (1400, 78, 'background .service-hero'),
    'assets/img/video-creator-hero.jpg':          (1400, 78, 'background .service-hero'),
    # Portfolio (dipakai .pf-feature ~1112px & .portfolio-shot ~380px)
    'assets/img/portfolio/editor-id.png':         (1200, 82, 'pf-feature 1112px'),
    'assets/img/portfolio/yoterpal.png':          (1200, 82, 'pf-feature 1112px'),
    'assets/img/portfolio/surendo.png':           (1200, 82, 'pf-feature 1112px'),
    'assets/img/portfolio/muslimhub-app.png':     (1200, 82, 'pf-feature 1112px'),
    'assets/img/portfolio/kasirstok.png':         (1200, 82, 'pf-feature 1112px'),
    'assets/img/portfolio/editor-id-app.png':     (1200, 82, 'pf-feature 1112px'),
    'assets/img/portfolio/devicescope.png':       (1200, 82, 'pf-feature 1112px'),
    'assets/img/portfolio/yoterpal-mobile.png':   (560,  82, 'galeri 2 kolom ~540px'),
    # Produk (mockup ponsel 178px + kartu galeri ~600px)
    'assets/img/products/websekolah-home.webp':   (760,  76, 'galeri produk'),
    'assets/img/products/aksi-crm-login.webp':    (760,  76, 'galeri produk'),
    'assets/img/products/ridesip-home.webp':      (760,  76, 'mockup ponsel beranda'),
    'assets/img/products/ridesip-admin.webp':     (760,  76, 'galeri produk'),
    'assets/img/products/aksisoft-pos-login.webp':(760,  76, 'galeri produk'),
    'assets/img/products/aksi-crm-dashboard.png': (760,  78, 'screenshot dasbor'),
    'assets/img/products/aksisoft-pos-dashboard.png': (760, 78, 'screenshot dasbor'),
    'assets/img/products/muslimhub-poster.jpg':   (800,  80, 'poster'),
    'assets/img/products/ridesip-logo.png':       (200,  90, 'logo kecil'),
    # Payment
    'assets/img/qris-aksisoft.jpg':               (820,  84, 'QR 340px + bisa dibuka penuh'),
}
# Poster video (semua di assets/videos/posters) -> kartu ~300px
POSTER_DIR = 'assets/videos/posters'
POSTER_TARGET = (420, 78, 'thumbnail .video-card ~300px')

# Pengecualian: jangan pernah ditulis ulang ke webp
NEVER_REWRITE = ('assets/img/og/', 'assets/downloads/', 'favicon.png', 'apple-touch-icon.png')

def collect():
    jobs = []
    for rel, (w, q, why) in RULES.items():
        jobs.append((rel, w, q, why))
    if os.path.isdir(os.path.join(ROOT, POSTER_DIR)):
        for f in sorted(os.listdir(os.path.join(ROOT, POSTER_DIR))):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                jobs.append((f'{POSTER_DIR}/{f}', *POSTER_TARGET))
    return jobs

def convert(rel, target_w, quality):
    src = os.path.join(ROOT, rel)
    if not os.path.exists(src):
        return None
    ow, oh = Image.open(src).size
    src_kb = round(os.path.getsize(src) / 1024, 1)
    im = Image.open(src)
    im.load()
    has_alpha = im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info)
    im = im.convert('RGBA' if has_alpha else 'RGB')
    w, h = im.size
    if w > target_w:
        nh = round(h * target_w / w)
        im = im.resize((target_w, nh), Image.LANCZOS)
        w, h = im.size
    out_rel = os.path.splitext(rel)[0] + '.webp'
    out = os.path.join(ROOT, out_rel)
    if APPLY:
        im.save(out, 'WEBP', quality=quality, method=6, exact=True)
    return {
        'src': rel, 'dst': out_rel,
        'old': (ow, oh), 'new': (w, h),
        'src_kb': src_kb,
        'kb': round(os.path.getsize(out) / 1024, 1) if (APPLY and os.path.exists(out)) else None,
    }

def main():
    results = []
    for rel, tw, q, why in collect():
        r = convert(rel, tw, q)
        if r is None:
            print('LEWAT (tidak ada):', rel); continue
        r['why'] = why
        results.append(r)

    print(f"{'SOURCE':52} {'ASLI':>11} {'BARU':>11} {'KB':>8} {'->':>7} {'KB':>8}")
    print('-' * 104)
    tot_old = tot_new = 0
    for r in sorted(results, key=lambda x: -(x['old'][0]*x['old'][1])):
        tot_old += r['src_kb']
        tot_new += (r['kb'] or 0)
        print(f"{r['src']:52} {r['old'][0]:>5}x{r['old'][1]:<5} {r['new'][0]:>5}x{r['new'][1]:<5} "
              f"{r['src_kb']:>8.0f} {(str(r['kb'])+'w') if r['kb'] else '  -  ':>7}")
    print('-' * 104)
    print(f"TOTAL: {tot_old:.0f} KB -> {tot_new:.0f} KB" +
          (f"  ({100-tot_new/tot_old*100:.0f}% lebih kecil)" if tot_new else ''))
    json.dump(results, open('/tmp/optimgs.json', 'w'), indent=1)
    if not APPLY:
        print('\nDRY-RUN. Tambahkan --apply untuk mengeksekusi.')

if __name__ == '__main__':
    main()
