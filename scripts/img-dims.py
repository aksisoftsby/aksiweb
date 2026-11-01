#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
img-dims.py — Tulis _data/imgdims.json berisi lebar/tinggi tiap gambar lokal.
Dipakai layout untuk atribut width/height (mencegah CLS / Cumulative Layout Shift).

    python3 scripts/img-dims.py
Jalankan ulang setelah menambah/mengganti gambar.
"""
import os, json
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ['assets/img', 'assets/videos/posters']

dims = {}
for d in DIRS:
    base = os.path.join(ROOT, d)
    if not os.path.isdir(base):
        continue
    for dp, dn, fn in os.walk(base):
        for f in fn:
            if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg')):
                continue
            p = os.path.join(dp, f)
            rel = '/' + os.path.relpath(p, ROOT).replace(os.sep, '/')
            try:
                if f.lower().endswith('.svg'):
                    s = open(p, encoding='utf-8', errors='ignore').read(4000)
                    import re
                    m = re.search(r'viewBox="[^"]*\s([\d.]+)\s+([\d.]+)"', s)
                    if not m:
                        m = re.search(r'width="([\d.]+)"\s+height="([\d.]+)"', s)
                    if m:
                        dims[rel] = {'w': int(float(m.group(1))), 'h': int(float(m.group(2)))}
                    continue
                with Image.open(p) as im:
                    dims[rel] = {'w': im.size[0], 'h': im.size[1]}
            except Exception as e:
                print('skip', rel, e)

out = os.path.join(ROOT, '_data', 'imgdims.json')
json.dump(dims, open(out, 'w', encoding='utf-8'), indent=0, sort_keys=True)
print(f'{len(dims)} gambar -> _data/imgdims.json')
