#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix-h1.py — Dalam konten Markdown, turunkan "# Judul" menjadi "## Judul"
karena layout sudah mencetak <h1> dari front matter (satu h1 per halaman).
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
targets = glob.glob(os.path.join(ROOT, '_ebooks', '*.md')) + \
          glob.glob(os.path.join(ROOT, '_posts', '*.md')) + \
          glob.glob(os.path.join(ROOT, '_articles', '*.md')) + \
          glob.glob(os.path.join(ROOT, '_portfolio', '*.md')) + \
          glob.glob(os.path.join(ROOT, '_websites', '*.md'))

fixed = 0
for p in targets:
    s = open(p, encoding='utf-8').read()
    m = re.match(r'(---\n.*?\n---\n)(.*)$', s, re.S)
    if not m:
        continue
    fm, body = m.group(1), m.group(2)
    new_body = re.sub(r'(?m)^#(?!#)\s', '## ', body)
    if new_body != body:
        open(p, 'w', encoding='utf-8').write(fm + new_body)
        fixed += 1
print(f'File dengan h1 ganda diperbaiki: {fixed}')
