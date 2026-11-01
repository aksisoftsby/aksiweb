#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rewrite-img-refs.py — Mengarahkan ulang semua referensi gambar di source ke
versi .webp hasil scripts/opt-imgs.py, lalu (opsional) menghapus file aslinya.

Pemakaian:
    python3 scripts/rewrite-img-refs.py                  # dry-run + laporan
    python3 scripts/rewrite-img-refs.py --apply          # tulis ulang
    python3 scripts/rewrite-img-refs.py --apply --purge  # + hapus file asli
"""
import os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = '--apply' in sys.argv
PURGE = '--purge' in sys.argv
SKIP_DIRS = {'_site', '.git', 'node_modules', 'vendor', '.jekyll-cache', 'tmp'}
SKIP_PATHS = ('assets/img/og/', 'assets/downloads/')

inv = json.load(open('/tmp/optimgs.json'))
# basename asli (dengan ekstensi) -> ekstensi baru, dan rel path untuk purge
ext_map = {}
originals = []
for r in inv:
    src, dst = r['src'], r['dst']
    if src.endswith('.webp'):
        continue                      # sudah webp, tidak perlu ditulis ulang
    ext_map[os.path.basename(src)] = os.path.splitext(dst)[1]
    originals.append(src)

pat = re.compile(r'([^\'"\s()<>]+?)\.(jpe?g|png)', re.I)

changed = {}
scanned = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in SKIP_DIRS]
    for f in fn:
        if not f.lower().endswith(('.md', '.html', '.css', '.yml', '.json', '.js', '.txt', '.liquid')):
            continue
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, ROOT)
        if any(s in rel for s in SKIP_PATHS):
            continue
        scanned += 1
        try:
            s = open(p, encoding='utf-8').read()
        except Exception:
            continue
        hits = []

        def sub(m):
            stem, ext = m.group(1), m.group(2)
            base = os.path.basename(stem) + '.' + ext.lower()
            if base in ext_map:
                new = stem + ext_map[base]
                hits.append(f'{stem}.{ext} -> {os.path.basename(new)}')
                return new
            return m.group(0)

        out = pat.sub(sub, s)
        if hits:
            changed[rel] = hits
            if APPLY:
                open(p, 'w', encoding='utf-8').write(out)

for rel, hits in sorted(changed.items()):
    uniq = sorted(set(hits))
    print(f'{rel}  ({len(hits)}x)')
    for h in uniq[:3]:
        print('    ', h)
    if len(uniq) > 3:
        print(f'     ... +{len(uniq)-3} lagi')

print(f'\nFile dipindai: {scanned} | File diubah: {len(changed)} | Referensi: '
      f'{sum(len(v) for v in changed.values())}')

if APPLY and PURGE:
    removed = freed = 0
    for rel in sorted(set(originals)):
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            freed += os.path.getsize(p)
            os.remove(p)
            removed += 1
    print(f'Hapus file asli: {removed} | {freed/1048576:.1f} MB dibebaskan')
elif not APPLY:
    print('\nDRY-RUN. Tambahkan --apply (opsional --purge) untuk mengeksekusi.')
