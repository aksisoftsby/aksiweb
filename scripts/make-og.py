#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make-og.py — Hasilkan gambar sosial (og:image) 1200x630 JPG untuk halaman
penting, supaya preview di WhatsApp / Telegram / Facebook / X tampil benar.

Mode:
  bg    : gambar jadi latar penuh + scrim burgundy + teks kiri
  frame : latar gradasi + screenshot dalam bingkai browser di kanan + teks kiri
  text  : gradasi saja + teks

Pemakaian: python3 scripts/make-og.py
"""
import os, re, sys, json, glob
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'assets', 'img', 'og')
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 630
BURG, BURG_DEEP, BURG_LIGHT = (93, 10, 23), (58, 12, 25), (143, 15, 34)
PINK = (243, 200, 207)
WHITE = (255, 255, 255)

def font(name, size):
    return ImageFont.truetype(f'/usr/share/fonts/truetype/lato/Lato-{name}.ttf', size)

BOLD = lambda s: font('Bold', s)
BLACK = lambda s: font('Black', s)
MED = lambda s: font('Medium', s)


def gradient(c1=BURG_DEEP, c2=BURG_LIGHT):
    """Gradasi diagonal burgundy: kiri-atas gelap, kanan-bawah terang."""
    base = Image.new('RGB', (W, H), c1)
    d = ImageDraw.Draw(base)
    for x in range(W):
        t = x / W
        d.line([(x, 0), (x, H)],
               fill=tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
    # sedikit penajaman tone ke arah bawah
    shade = Image.new('L', (1, H))
    for y in range(H):
        shade.putpixel((0, y), int(26 * (1 - y / H) ** 1.6))
    dark = Image.new('RGB', (W, H), (24, 4, 12))
    base = Image.composite(base, dark, shade.resize((W, H)))
    return base


def cover(im, w, h):
    """Resize lalu crop tengah ke w x h."""
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = (im.width - w) // 2
    y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def contain(im, w, h):
    s = min(w / im.width, h / im.height)
    return im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)


def tracked(draw, xy, text, fnt, fill, spacing=3):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + spacing
    return x


def wrap(draw, text, fnt, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines[:3]


def brand_footer(draw, sub='aksisoft.web.id'):
    f = MED(21)
    draw.rounded_rectangle((64, H - 74, 64 + 10, H - 74 + 10), 3, fill=PINK)
    draw.text((84, H - 78), sub, font=f, fill=(255, 255, 255, 200))


def text_block(img, kicker, title, sub=None):
    d = ImageDraw.Draw(img, 'RGBA')
    x, y = 64, 96
    tracked(d, (x, y), kicker.upper(), MED(20), PINK, 4)
    y += 46
    for line in wrap(d, title, BLACK(52), 520):
        d.text((x, y), line, font=BLACK(52), fill=(255, 255, 255, 255))
        y += 62
    if sub:
        y += 8
        for line in wrap(d, sub, MED(24), 500):
            d.text((x, y), line, font=MED(24), fill=(255, 240, 240, 215))
            y += 32
    brand_footer(d)
    return img


def scrim(img, strong=215):
    """Gelap di kiri, transparan di kanan, agar teks selalu terbaca."""
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    for x in range(W):
        a = int(strong * (1 - x / W) ** 1.25)
        od.line([(x, 0), (x, H)], fill=(40, 6, 16, a))
    img.alpha_composite(ov)
    return img


def browser(img, src, area=(624, 86, 1152, 544)):
    """Bingkai browser yang tingginya mengikuti rasio gambar (tanpa letterbox)."""
    ax0, ay0, ax1, ay1 = area
    aw, ah = ax1 - ax0, ay1 - ay0
    bar = 42
    a = src.width / src.height
    body_w = min(aw, int((ah - bar - 24) * a))
    body_h = max(120, round(body_w / a))
    fw, fh = body_w + 24, body_h + bar + 24
    x0 = ax0 + (aw - fw) // 2
    y0 = ay0 + (ah - fh) // 2

    frame = Image.new('RGBA', (fw, fh), (255, 255, 255, 255))
    fd = ImageDraw.Draw(frame)
    fd.rectangle((0, 0, fw, bar), fill=(246, 232, 234, 255))
    for i, c in enumerate([(224, 99, 122), (230, 169, 91), (95, 185, 138)]):
        fd.ellipse((16 + i * 20, 15, 26 + i * 20, 25), fill=c)
    shot = contain(src.convert('RGB'), body_w, body_h)
    frame.paste(shot, ((fw - shot.width) // 2, bar + (fh - bar - shot.height) // 2))
    mask = Image.new('L', frame.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, fw, fh), 18, fill=255)
    sh = Image.new('RGBA', (fw + 8, fh + 8), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((4, 4, fw + 4, fh + 4), 20, fill=(0, 0, 0, 80))
    img.alpha_composite(sh, (x0 - 4, y0 - 4))
    img.paste(frame, (x0, y0), mask)
    return img


def save(img, name):
    p = os.path.join(OUT, name)
    img.convert('RGB').save(p, 'JPEG', quality=86, optimize=True, progressive=True)
    print(f'  {name:44} {os.path.getsize(p) / 1024:6.1f} KB')


def img(rel):
    return Image.open(os.path.join(ROOT, rel.lstrip('/')))


def make_bg(src, name, kicker, title, sub=None):
    base = cover(img(src), W, H).convert('RGBA')
    base = scrim(base)
    text_block(base, kicker, title, sub)
    save(base, name)


def make_frame(src, name, kicker, title, sub=None):
    base = gradient().convert('RGBA')
    if src:
        base = browser(base, img(src))
    text_block(base, kicker, title, sub)
    save(base, name)


def make_text(name, kicker, title, sub=None):
    base = gradient().convert('RGBA')
    text_block(base, kicker, title, sub)
    save(base, name)


# ------------------------------------------------------------------ daftar
HERO = 'assets/img/aksisoft-hero-burgundy.webp'

print('Default + halaman utama:')
make_frame(HERO, 'aksisoft-og.jpg', 'Aksisoft Media',
           'Jasa Pembuatan Website Profesional',
           'Website, aplikasi, dan sistem digital yang cepat, modern, dan terpercaya.')
make_text('layanan-og.jpg', 'Layanan', 'Layanan Digital Aksisoft',
          'Website, video, aplikasi, iklan, dan email marketing.')
make_text('produk-og.jpg', 'Produk', 'Produk Digital Aksisoft',
          'RideSip, Aksi CRM, AksiSoft POS, WebSekolah, MuslimHub.')
make_text('portfolio-og.jpg', 'Portfolio', 'Hasil Kerja Aksisoft',
          'Website, aplikasi Android, dan konten video yang sudah tayang.')
make_text('kontak-og.jpg', 'Kontak', 'Mari Bangun Solusi Digital Anda',
          'Konsultasi gratis tanpa komitmen.')
make_text('tentang-og.jpg', 'Tentang', 'Tentang Aksisoft Media',
          'Dari kebutuhan, menjadi solusi digital.')
make_frame('assets/img/qris-aksisoft.webp', 'payment-og.jpg', 'Pembayaran',
           'Bayar dengan QRIS', 'Satu QRIS untuk semua aplikasi pembayaran.')
make_text('website-og.jpg', 'Katalog', 'Template Website Siap Pakai',
          '30+ template HTML untuk berbagai kebutuhan bisnis.')
make_text('ebook-og.jpg', 'eBook', 'eBook & Worksheet Anak',
          'Belajar menulis, mewarnai, dan kuis interaktif.')

print('\nLayanan:')
SERVICES = [
    ('website-static', 'Jasa Pembuatan Website Static', 'Cepat, aman, dan SEO-ready',
     'assets/img/website-static-hero.webp'),
    ('website-news-dynamic', 'Jasa Website News Dynamic', 'Portal berita dengan CMS mudah',
     'assets/img/website-news-dynamic-hero.webp'),
    ('video-editing', 'Content Creator Video', 'Reels, promosi, dan company profile',
     'assets/img/video-creator-hero.webp'),
    ('aplikasi-custom-android', 'Aplikasi Custom & Android', 'Dari konsep hingga Google Play',
     'assets/img/aplikasi-custom-android-hero.webp'),
    ('email-marketing', 'Jasa Email Marketing', 'Newsletter, kampanye, dan otomasi',
     'assets/img/email-marketing-hero.webp'),
    ('google-ads', 'Jasa Google Ads', 'Iklan pencarian yang terukur',
     'assets/img/google-ads-hero.webp'),
    ('social-media-ads', 'Jasa Social Media Ads', 'Meta dan TikTok Ads yang menjual',
     'assets/img/social-media-ads-hero.webp'),
]
for slug, title, sub, src in SERVICES:
    make_bg(src, f'layanan-{slug}.jpg', 'Layanan', title, sub)

print('\nPortfolio:')
PORTFOLIO = [
    ('editor-id', 'Editor.id', 'Portal berita & referensi Indonesia', 'assets/img/portfolio/editor-id.webp'),
    ('surendo', 'Surendo', 'Website CV. Surya Energy Indonesia', 'assets/img/portfolio/surendo.webp'),
    ('yoterpal', 'YO Tarpaulin', 'Website produsen terpal nasional', 'assets/img/portfolio/yoterpal.webp'),
    ('kasirstok', 'KasirStok', 'Aplikasi Android kasir & stok UMKM', 'assets/img/portfolio/kasirstok.webp'),
    ('devicescope', 'DeviceScope', 'Aplikasi info perangkat Android', 'assets/img/portfolio/devicescope.webp'),
    ('editor-id-app', 'Editor.id News', 'Aplikasi berita di Google Play', 'assets/img/portfolio/editor-id-app.webp'),
    ('muslimhub-app', 'MuslimHub', 'Portal ibadah web & Android', 'assets/img/portfolio/muslimhub-app.webp'),
]
for slug, title, sub, src in PORTFOLIO:
    make_frame(src, f'portfolio-{slug}.jpg', 'Portfolio', title, sub)

print('\nProduk:')
PRODUCTS = [
    ('ridesip', 'RideSip', 'Superapp layanan lokal', 'assets/img/products/ridesip-home.webp'),
    ('aksi-crm', 'Aksi CRM', 'CRM & operasional pelanggan', 'assets/img/products/aksi-crm-dashboard.webp'),
    ('aksisoft-pos', 'AksiSoft POS', 'Kasir & operasional ritel', 'assets/img/products/aksisoft-pos-dashboard.webp'),
    ('websekolah', 'WebSekolah + PPDB', 'Website sekolah & pendaftaran online', 'assets/img/products/websekolah-home.webp'),
    ('muslimhub', 'MuslimHub', 'Portal ibadah web & Android', 'assets/img/products/muslimhub-og.jpg'),
    ('ai-chat', 'Aksisoft AI Chat', 'Asisten AI untuk bisnis', None),
]
for slug, title, sub, src in PRODUCTS:
    if src:
        make_frame(src, f'produk-{slug}.jpg', 'Produk', title, sub)
    else:
        make_text(f'produk-{slug}.jpg', 'Produk', title, sub)

print('\nBlog:')
BLOG = [
    ('membuat-artikel-seo', 'Panduan Lengkap Membuat Artikel SEO'),
    ('cara-memilih-jasa-pembuatan-website', 'Cara Memilih Jasa Pembuatan Website'),
    ('checklist-seo-website-baru', 'Checklist SEO untuk Website Baru'),
    ('kenapa-github-pages-cocok-untuk-website-bisnis', 'Kenapa GitHub Pages Cocok untuk Bisnis'),
]
for slug, title in BLOG:
    make_text(f'blog-{slug}.jpg', 'Blog Aksisoft', title, 'aksisoft.web.id/blog')


print('\nKatalog template & eBook (dari front matter):')


def fm_get(text, key):
    m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', text, re.M)
    return m.group(1) if m else ''


def name_of(title):
    for sep in (' - ', ' – ', ' — ', ' | '):
        if sep in title:
            return title.split(sep)[0].strip()
    return title


td_path = os.path.join(ROOT, '_data', 'templatedims.json')
tdims = json.load(open(td_path)) if os.path.exists(td_path) else {}

for p in sorted(glob.glob(os.path.join(ROOT, '_websites', '*.md'))):
    slug = os.path.splitext(os.path.basename(p))[0]
    head = open(p, encoding='utf-8').read().split('---')[1]
    title = name_of(fm_get(head, 'seo_title') or fm_get(head, 'title'))
    sub = fm_get(head, 'description')[:96]
    shots = tdims.get(slug, {}).get('shots', {})
    src = None
    for cand in shots.get('thumb', []) + shots.get('desktop', []):
        fp = os.path.join(ROOT, cand.lstrip('/'))
        if os.path.exists(fp):
            src = cand          # path relatif dari root, dipakai make_frame()
            break
    kicker = 'Template Website'
    if src:
        make_frame(src, f'website-{slug}.jpg', kicker, title, sub)
    else:
        make_text(f'website-{slug}.jpg', kicker, title, sub)

for p in sorted(glob.glob(os.path.join(ROOT, '_ebooks', '*.md'))):
    slug = os.path.splitext(os.path.basename(p))[0]
    head = open(p, encoding='utf-8').read().split('---')[1]
    title = name_of(fm_get(head, 'title'))
    cover = fm_get(head, 'image')
    sub = fm_get(head, 'description')[:96]
    if cover.startswith('/assets/') and os.path.exists(ROOT + cover):
        make_frame(cover, f'ebook-{slug}.jpg', 'eBook & Worksheet', title, sub)
    else:
        make_text(f'ebook-{slug}.jpg', 'eBook & Worksheet', title, sub)

print('\nSelesai.')
