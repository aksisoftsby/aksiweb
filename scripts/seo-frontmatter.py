#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
seo-frontmatter.py — Menambah/memperbaiki front matter SEO:
  * seo_title ringkas untuk 55 halaman template (_websites) dan 200 halaman
    layanan-per-kota (_seo_articles) supaya <title> <= 58 karakter,
  * og_image untuk halaman-halaman kunci.

Jalankan: python3 scripts/seo-frontmatter.py
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- 1. _websites
CATS = [
    (r'wedding|invitation', 'Undangan Pernikahan'),
    (r'restaurant|restoran|kopi|coffee|bakery|cafe|wok|dining|warung|kuliner|rasa|pawonara|wedang|joglara|larasaji|nusawiji|rosojowo|sajiwara|sekarsara|sekarsa|ndalemasa|pendhapa|gandhul|morvana|mellow|glaze|tea house', 'Restoran & Kuliner'),
    (r'school|academy|collegiate|campus|eduvanguard|schola|vibranted|vocapro|kreativa', 'Sekolah'),
    (r'hotel|resort|villa|hospitality|grand', 'Hotel & Resor'),
    (r'pet |pet,|veterinary|grooming|paw', 'Pet Care'),
    (r'car |auto|motors|dealer|mechanic|vehicle', 'Otomotif'),
    (r'news|magazine|editorial|portal|press', 'Portal Berita'),
    (r'skincare|spa|wellness|beauty|aesthetic', 'Kecantikan & Spa'),
    (r'law|legal', 'Firma Hukum'),
    (r'gym|fitness', 'Gym & Kebugaran'),
    (r'travel', 'Travel'),
    (r'wealth|ledger|financ', 'Keuangan'),
    (r'storefront|shop|olshop|e-commerce', 'Toko Online'),
    (r'band|music', 'Musik & Band'),
    (r'studio|digital|saas|creative|technolog|agensi|nexora|velora|pixelra', 'Agensi & Studio'),
    (r'industrial', 'Industri'),
]


def classify(text):
    low = text.lower()
    for pat, label in CATS:
        if re.search(pat, low):
            return label
    return 'Company Profile'


def name_of(title):
    for sep in (' - ', ' – ', ' — '):
        if sep in title:
            return title.split(sep)[0].strip()
    m = re.match(r'^(.*?)(?:\s+(?:Static|Template|HTML).*)$', title)
    return (m.group(1) if m else title).strip()


n = 0
for p in sorted(glob.glob(os.path.join(ROOT, '_websites', '*.md'))):
    s = open(p, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n', s, re.S)
    if not m:
        continue
    fm = m.group(1)
    tm = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm, re.M)
    if not tm:
        continue
    name = name_of(tm.group(1).strip())
    cat = classify(tm.group(1))
    seo = f'{name} — Template {cat}'
    had = re.search(r'^seo_title:\s*"?([^"\n]+)"?\s*$', fm, re.M)
    if had and had.group(1).strip() == seo:
        continue
    if had:
        fm_new = fm[:had.start()] + f'seo_title: "{seo}"' + fm[had.end():]
    else:
        fm_new = fm + f'\nseo_title: "{seo}"'
    open(p, 'w', encoding='utf-8').write(s.replace(fm, fm_new, 1))
    n += 1
print(f'_websites  : seo_title ditulis/perbarui di {n} file')

# ------------------------------------------------------------- 2. _seo_articles
n = 0
for p in sorted(glob.glob(os.path.join(ROOT, '_seo_articles', '*.md'))):
    s = open(p, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n', s, re.S)
    if not m:
        continue
    fm = m.group(1)
    if re.search(r'^seo_title:', fm, re.M):
        continue
    lab = re.search(r'^service_label:\s*"?([^"\n]+)"?\s*$', fm, re.M)
    city = re.search(r'^city:\s*"?([^"\n]+)"?\s*$', fm, re.M)
    if not (lab and city):
        continue
    l, c = lab.group(1).strip(), city.group(1).strip()
    if c.lower().startswith('surakarta'):
        c = 'Surakarta'
    seo = f'{l} {c}'
    fm_new = fm + f'\nseo_title: "{seo}"'
    open(p, 'w', encoding='utf-8').write(s.replace(fm, fm_new, 1))
    n += 1
print(f'_seo_articles: seo_title ditambahkan ke {n} file')

# ---------------------------------------------------------------- 3. og_image
OG = {}
for f in glob.glob(os.path.join(ROOT, 'assets/img/og', '*.jpg')):
    OG[os.path.basename(f)] = '/assets/img/og/' + os.path.basename(f)

MAP = {
    'index.html': 'aksisoft-og.jpg',
    'pages/layanan.md': 'layanan-og.jpg',
    'pages/produk.md': 'produk-og.jpg',
    'pages/portfolio.md': 'portfolio-og.jpg',
    'pages/kontak.md': 'kontak-og.jpg',
    'pages/tentang.md': 'tentang-og.jpg',
    'pages/payment.md': 'payment-og.jpg',
    'pages/website.html': 'website-og.jpg',
    'pages/ebook.html': 'ebook-og.jpg',
    'pages/artikel.md': 'portfolio-og.jpg',
    'pages/blog.html': 'portfolio-og.jpg',
    'pages/privacy-policy.md': 'tentang-og.jpg',
    'pages/privacy-policy-devicescope.md': 'tentang-og.jpg',
    'pages/privacy-policy-aksifile.md': 'tentang-og.jpg',
    'pages/privacy-policy-aksioffice.md': 'tentang-og.jpg',
    'pages/layanan/website-static.md': 'layanan-website-static.jpg',
    'pages/layanan/website-news-dynamic.md': 'layanan-website-news-dynamic.jpg',
    'pages/layanan/video-editing.md': 'layanan-video-editing.jpg',
    'pages/layanan/aplikasi-custom-android.md': 'layanan-aplikasi-custom-android.jpg',
    'pages/layanan/email-marketing.md': 'layanan-email-marketing.jpg',
    'pages/layanan/google-ads.md': 'layanan-google-ads.jpg',
    'pages/layanan/social-media-ads.md': 'layanan-social-media-ads.jpg',
    'pages/produk-ridesip.md': 'produk-ridesip.jpg',
    'pages/produk-aksi-crm.md': 'produk-aksi-crm.jpg',
    'pages/produk-aksisoft-pos.md': 'produk-aksisoft-pos.jpg',
    'pages/produk-websekolah.md': 'produk-websekolah.jpg',
    'pages/produk-muslimhub.md': 'produk-muslimhub.jpg',
    'pages/produk-ai-chat.md': 'produk-ai-chat.jpg',
    '_portfolio/editor-id.md': 'portfolio-editor-id.jpg',
    '_portfolio/surendo.md': 'portfolio-surendo.jpg',
    '_portfolio/yoterpal.md': 'portfolio-yoterpal.jpg',
    '_portfolio/kasirstok.md': 'portfolio-kasirstok.jpg',
    '_portfolio/devicescope.md': 'portfolio-devicescope.jpg',
    '_portfolio/editor-id-app.md': 'portfolio-editor-id-app.jpg',
    '_portfolio/muslimhub-app.md': 'portfolio-muslimhub-app.jpg',
}
for p in glob.glob(os.path.join(ROOT, '_posts', '*.md')):
    slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', os.path.basename(p)[:-3])
    MAP[os.path.relpath(p, ROOT)] = f'blog-{slug}.jpg'

# katalog: og_image per halaman detail (dibuat scripts/make-og.py)
for p in glob.glob(os.path.join(ROOT, '_websites', '*.md')):
    slug = os.path.basename(p)[:-3]
    if f'website-{slug}.jpg' in OG:
        MAP[os.path.relpath(p, ROOT)] = f'website-{slug}.jpg'
for p in glob.glob(os.path.join(ROOT, '_ebooks', '*.md')):
    slug = os.path.basename(p)[:-3]
    if f'ebook-{slug}.jpg' in OG:
        MAP[os.path.relpath(p, ROOT)] = f'ebook-{slug}.jpg'

added = 0
for rel, img in MAP.items():
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print('  LEWAT (file tidak ada):', rel)
        continue
    if img not in OG:
        print('  LEWAT (og tidak ada):', img)
        continue
    s = open(p, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n', s, re.S)
    if not m:
        print('  LEWAT (tanpa front matter):', rel)
        continue
    fm = m.group(1)
    if re.search(r'^og_image:', fm, re.M):
        continue
    open(p, 'w', encoding='utf-8').write(s.replace(fm, fm + f"\nog_image: '/assets/img/og/{img}'", 1))
    added += 1
print(f'og_image   : ditambahkan ke {added} file')
