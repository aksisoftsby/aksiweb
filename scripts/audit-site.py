#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit-site.py — Satu perintah untuk memeriksa hasil build di _site/.

Menggabungkan pengecekan yang dulu tersebar (jumlah halaman, panjang title &
description, validitas JSON-LD, kelengkapan <img>, og:image, canonical, dan
tautan aset yang rusak). Keluaran ringkas: baris "OK" atau daftar temuan.

Pemakaian:
    python3 scripts/audit-site.py            # periksa _site/
    python3 scripts/audit-site.py --top      # + 10 halaman paling berat
"""
import os, re, sys, json, collections

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_site')
TOP = '--top' in sys.argv

pages = []
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('.git',)]
    for f in fn:
        if f.endswith('.html'):
            pages.append(os.path.join(dp, f))

title_long, desc_long, no_desc = [], [], []
bad_jsonld, no_og, no_canon = [], [], []
no_alt, no_dim, remote_img, broken_ref = [], [], [], []
img_total = 0
ext_count = collections.Counter()
types = collections.Counter()

IMG_RE = re.compile(r'<img\b[^>]*>', re.I | re.S)
LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.I | re.S)

for p in pages:
    rel = '/' + os.path.relpath(p, ROOT).replace(os.sep, '/')
    s = open(p, encoding='utf-8', errors='ignore').read()

    t = re.search(r'<title>(.*?)</title>', s, re.S)
    if t:
        txt = re.sub(r'&#\d+;|&[a-z]+;', 'x', t.group(1)).strip()
        if len(txt) > 60:
            title_long.append((len(txt), rel, txt))

    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not d or not d.group(1).strip():
        no_desc.append(rel)
    elif len(d.group(1)) > 160:
        desc_long.append((len(d.group(1)), rel))

    if not re.search(r'(property="og:image"|name="twitter:image")', s):
        no_og.append(rel)

    if '/assets/' in s and not re.search(r'rel="canonical"', s):
        no_canon.append(rel)

    for m in LD_RE.finditer(s):
        try:
            data = json.loads(m.group(1))
            graph = data.get('@graph') if isinstance(data, dict) else None
            for node in (graph or [data]):
                if isinstance(node, dict):
                    for ty in ([node['@type']] if isinstance(node.get('@type'), str)
                               else (node.get('@type') or [])):
                        types[ty] += 1
        except Exception as e:
            bad_jsonld.append((rel, str(e)[:60]))

    for tag in IMG_RE.findall(s):
        if 'src=' not in tag:
            continue
        img_total += 1
        src = re.search(r'src="([^"]+)"', tag)
        url = src.group(1) if src else ''
        if url.startswith('http'):
            remote_img.append((rel, url[:70]))
        elif url.startswith('/'):
            ext_count[os.path.splitext(url)[1].lstrip('.')] += 1
            if not os.path.exists(ROOT + url.split('?')[0]):
                broken_ref.append((rel, url))
        if not re.search(r'\balt=', tag):
            no_alt.append((rel, url[:60]))
        if not ('width=' in tag and 'height=' in tag):
            no_dim.append((rel, url[:60]))

print(f'halaman              : {len(pages)}')
print(f'<img> total          : {img_total}  {dict(ext_count)}')
print(f'remote (host lain)   : {len(remote_img)}')
print(f'aset lokal hilang    : {len(broken_ref)}')
print(f'<img> tanpa alt      : {len(no_alt)}')
print(f'<img> tanpa dimensi  : {len(no_dim)}')
print(f'title > 60 karaktter : {len(title_long)}')
print(f'description > 160    : {len(desc_long)}')
print(f'tanpa description    : {len(no_desc)}')
print(f'tanpa og:image       : {len(no_og)}')
print(f'tanpa canonical      : {len(no_canon)}')
print(f'JSON-LD tidak valid  : {len(bad_jsonld)}')

fail = 0
for label, items in (
    ('aset hilang', broken_ref), ('JSON-LD rusak', bad_jsonld),
    ('title kepanjangan', title_long), ('desc kepanjangan', desc_long),
    ('img tanpa alt', no_alt), ('img tanpa dimensi', no_dim),
    ('tanpa og:image', no_og), ('tanpa description', no_desc),
    ('img remote', remote_img),
):
    if items:
        fail += len(items)
        print(f'\n-- {label} ({len(items)}):')
        for it in items[:8]:
            print('   ', it)

if TOP:
    print('\n-- 10 HTML terbesar:')
    sizes = sorted(((os.path.getsize(p) / 1024, '/' + os.path.relpath(p, ROOT).replace(os.sep, '/'))
                    for p in pages), reverse=True)[:10]
    for kb, rel in sizes:
        print(f'  {kb:7.1f} KB  {rel}')

print('\nTipe JSON-LD yang terbit:', dict(types.most_common()))
print('\nHASIL:', 'BERSIH' if fail == 0 else f'{fail} temuan perlu dicek')
sys.exit(0 if fail == 0 else 1)
