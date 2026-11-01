#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add-missing-alt.py — Mengisi atribut alt yang hilang pada <img>.
Untuk berkas cetak company profile (dipakai Chrome headless -> PDF) alt
dibuat dari nama berkas; gambar dekoratif kecil memakai alt="".

    python3 scripts/add-missing-alt.py
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS = ['company-profile.html', 'company-profile-en.html', 'proposal/indomandiri.html']

pat = re.compile(r'<img\b[^>]*>', re.I)


def alt_for(tag):
    m = re.search(r'src="([^"]+)"', tag)
    if not m:
        return None
    src = m.group(1)
    if src.startswith('data:') or src.endswith('.svg'):
        return ''                      # dekoratif
    stem = os.path.splitext(os.path.basename(src))[0]
    stem = re.sub(r'^[\d_.-]+|[\d_.-]+$', '', stem).replace('-', ' ').replace('_', ' ')
    stem = re.sub(r'\s+', ' ', stem).strip()
    if not stem:
        return ''
    return stem[:1].upper() + stem[1:]


n = 0
for rel in TARGETS:
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        continue
    s = open(p, encoding='utf-8').read()

    def sub(m):
        global n
        tag = m.group(0)
        if 'alt=' in tag.lower():
            return tag
        a = alt_for(tag)
        if a is None:
            return tag
        n += 1
        return tag[:-1] + f' alt="{a}">'

    out = pat.sub(sub, s)
    if out != s:
        open(p, 'w', encoding='utf-8').write(out)
        print(f'{rel}: {len(pat.findall(out))} <img> diperiksa')

print(f'alt ditambahkan: {n}')
