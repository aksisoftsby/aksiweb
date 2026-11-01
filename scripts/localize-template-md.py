#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
localize-template-md.py — Menyamakan _websites/<slug>.md dengan
_data/websites.json: URL screenshot-index.jpg yang masih remote diganti ke
thumbnail lokal hasil scripts/localize-remote-imgs.py, sehingga og:image dan
JSON-LD halaman template ikut menunjuk aset sendiri (bukan host lain).

    python3 scripts/localize-template-md.py            # lihat rencana
    python3 scripts/localize-template-md.py --apply    # tulis
"""
import os, re, sys, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = '--apply' in sys.argv

data = {it['slug']: it for it in json.load(open(os.path.join(ROOT, '_data', 'websites.json'), encoding='utf-8'))}

changed = 0
for p in sorted(glob.glob(os.path.join(ROOT, '_websites', '*.md'))):
    slug = os.path.splitext(os.path.basename(p))[0]
    it = data.get(slug)
    if not it:
        print('  LEWAT (tidak ada di websites.json):', slug)
        continue
    thumb = it.get('thumbnail') or ''
    if not thumb.startswith('/assets/'):
        print('  LEWAT (thumbnail belum lokal):', slug)
        continue
    s = open(p, encoding='utf-8').read()
    m = re.search(r'^image:\s*"?(https://template\.aksisoft\.web\.id/[^"\n]+)"?\s*$', s, re.M)
    if not m:
        continue
    new = s[:m.start()] + f'image: "{thumb}"' + s[m.end():]
    if new != s:
        changed += 1
        if APPLY:
            open(p, 'w', encoding='utf-8').write(new)
        print(f'  {slug}: image/og -> {thumb}')

print(f'\nFile diperbarui: {changed} dari {len(glob.glob(os.path.join(ROOT, "_websites", "*.md")))}')
if not APPLY:
    print('DRY-RUN. Tambahkan --apply.')
