#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-css.py — Gabungkan 11 stylesheet redesign menjadi satu assets/css/site.css.

Urutan MUSTAH diubah: redesign8/9/10 adalah normalisasi & override yang
harus dimuat paling belakang. Jalankan lagi setiap kali mengedit salah satu
file sumber, sebelum `jekyll build`.

    python3 scripts/build-css.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = [
    'products.css', 'catalog.css',
    'redesign.css', 'redesign2.css', 'redesign3.css', 'redesign4.css',
    'redesign5.css', 'redesign6.css', 'redesign7.css', 'redesign8.css',
    'redesign9.css', 'redesign10.css',
]
# style.css sengaja TIDAK di-bundle: tidak pernah di-link default.html,
# memasukkannya akan mengubah tampilan halaman yang sudah disetujui.
OUT = os.path.join(ROOT, 'assets', 'css', 'site.css')


def strip_comments(css):
    out, i, n = [], 0, len(css)
    while i < n:
        if css.startswith('/*', i):
            j = css.find('*/', i + 2)
            i = n if j < 0 else j + 2
        else:
            out.append(css[i]); i += 1
    return ''.join(out)


def minify(css):
    css = strip_comments(css)
    lines = []
    for ln in css.split('\n'):
        ln = ln.strip()
        if ln:
            lines.append(ln)
    css = '\n'.join(lines)
    # aman: hanya rapikan spasi di sekitar tanda baca, spasi dalam calc() utuh
    css = re.sub(r'\s*([{};:,])\s*', r'\1', css)
    css = re.sub(r'\s*>\s*', '>', css)
    css = re.sub(r'\n+', '\n', css)
    return css


def main():
    parts = []
    for name in SRC:
        p = os.path.join(ROOT, 'assets', 'css', name)
        if not os.path.exists(p):
            print('LEWAT (tidak ada):', name)
            continue
        raw = open(p, encoding='utf-8').read()
        parts.append(f'/*! {name} */\n' + minify(raw))
        print(f'  {name:16} {len(raw)/1024:6.1f} KB -> {len(minify(raw))/1024:5.1f} KB')
    bundle = '\n'.join(parts)
    open(OUT, 'w', encoding='utf-8').write(bundle)
    print(f'\nsite.css : {len(bundle)/1024:.1f} KB  ({len(SRC)} file digabung)')


if __name__ == '__main__':
    main()
