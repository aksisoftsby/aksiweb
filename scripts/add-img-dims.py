#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add-img-dims.py — Menambah width/height pada <img> yang belum punya, memakai
_data/imgdims.json. Aman untuk halaman cetak (company-profile*.html) karena CSS
halaman itu sudah menentukan ukuran sendiri; atribut ini hanya dipakai browser
untuk menghitung rasio sebelum gambar tiba (mencegah CLS).

    python3 scripts/add-img-dims.py                # lihat rencana
    python3 scripts/add-img-dims.py --apply        # tulis
"""
import os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = '--apply' in sys.argv
SKIP_DIRS = {'_site', '.git', 'node_modules', 'vendor', '.jekyll-cache'}

dims = json.load(open(os.path.join(ROOT, '_data', 'imgdims.json'), encoding='utf-8'))
by_base = {os.path.basename(k): v for k, v in dims.items()}

targets = []
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in SKIP_DIRS]
    for f in fn:
        if f.endswith(('.html', '.md')):
            targets.append(os.path.join(dp, f))

changed, added = 0, 0
for p in targets:
    s = open(p, encoding='utf-8').read()
    if '<img' not in s:
        continue

    def sub(m):
        global added
        tag = m.group(0)
        if 'width=' in tag or 'height=' in tag:
            return tag
        src = re.search(r'src="([^"]+)"', tag)
        if not src:
            return tag
        u = src.group(1)
        u = re.sub(r'^\{\{[^}]*\}\}', '', u).strip()
        d = dims.get('/' + u.lstrip('/')) or by_base.get(os.path.basename(u))
        if not d:
            return tag
        added += 1
        return tag[:4] + f' width="{d["w"]}" height="{d["h"]}" ' + tag[4:]

    out = re.sub(r'<img\b[^>]*>', sub, s)
    if out != s:
        changed += 1
        if APPLY:
            open(p, 'w', encoding='utf-8').write(out)
        print('  ', os.path.relpath(p, ROOT))

print(f'\nFile diubah: {changed} | <img> diberi dimensi: {added}')
if not APPLY:
    print('DRY-RUN. Tambahkan --apply.')
