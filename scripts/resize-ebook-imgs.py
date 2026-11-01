#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resize-ebook-imgs.py — Menyeragamkan ukuran gambar katalog eBook.

Cover dipakai di 3 tempat: kartu katalog (~260px), sampul halaman detail
(~300px), dan og:image. Screenshots pratinjau tampil di galeri ~320px.
Versi awal dilokalkan pada 800/900px (rata-rata 120 KB WebP), jadi dikecilkan
ke 620/720px. Sumber aslinya tetap ada di template.aksisoft.web.id, jadi proses
ini aman diulang.

    python3 scripts/resize-ebook-imgs.py           # lihat rencana
    python3 scripts/resize-ebook-imgs.py --apply   # tulis ulang file
"""
import os, sys, io, glob
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = '--apply' in sys.argv
RULES = [('cover-', 620, 76), ('screenshot-', 720, 74)]
DEFAULT = (720, 76)

rows = []
for p in sorted(glob.glob(os.path.join(ROOT, 'assets/img/ebook/*.webp'))):
    base = os.path.basename(p)
    width, q = next(((w, qq) for pre, w, qq in RULES if base.startswith(pre)), DEFAULT)
    im = Image.open(p)
    ow, oh = im.size
    if ow <= width:
        rows.append((base, ow, oh, ow, oh, os.path.getsize(p), os.path.getsize(p)))
        continue
    nh = round(oh * width / ow)
    old_size = os.path.getsize(p)
    im = im.convert('RGB').resize((width, nh), Image.LANCZOS)
    new_size = old_size
    if APPLY:
        tmp = p + '.tmp'
        im.save(tmp, 'WEBP', quality=q, method=6)
        new_size = os.path.getsize(tmp)
        os.replace(tmp, p)
    else:
        import io
        buf = io.BytesIO()
        im.save(buf, 'WEBP', quality=q, method=6)
        new_size = buf.tell()
    rows.append((base, ow, oh, width, nh, old_size, new_size))

before = sum(r[5] for r in rows)
after = sum(r[6] for r in rows)
print(f'{len(rows)} gambar ebook: {before/1048576:.1f} MB -> {after/1048576:.1f} MB')
print('contoh:')
for r in rows[:5]:
    print(f'  {r[0]:56} {r[1]}x{r[2]} -> {r[3]}x{r[4]}')
if not APPLY:
    print('\nDRY-RUN. Tambahkan --apply.')
