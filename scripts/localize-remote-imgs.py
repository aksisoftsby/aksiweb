#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
localize-remote-imgs.py — Unduh gambar yang selama ini di-host terpisah
(template.aksisoft.web.id) lalu simpan sebagai WebP berukuran pas di
assets/img/. Referensi di _data/*.json dan _ebooks/*.md ikut diperbarui.

    python3 scripts/localize-remote-imgs.py            # lihat rencana
    python3 scripts/localize-remote-imgs.py --apply    # unduh + tulis ulang
"""
import os, re, sys, json, io, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = '--apply' in sys.argv
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'

# (pola url, folder tujuan, lebar target, kualitas)
RULES = [
    (re.compile(r'/demo/(?P<slug>[^/]+)/screenshot-desktop/screenshot-index\.jpg'),
     'assets/img/templates', 760, 78, lambda m: f"{m.group('slug')}.webp"),
    (re.compile(r'/ebook/cover/(?P<stem>[^/]+)\.jpg'),
     'assets/img/ebook', 800, 80, lambda m: f"{m.group('stem')}.webp"),
    (re.compile(r'/ebook/screenshot/(?P<stem>[^/]+)\.jpg'),
     'assets/img/ebook', 900, 80, lambda m: f"{m.group('stem')}.webp"),
]


def gather():
    urls = set()
    for f in ['_data/websites.json', '_data/ebooks.json']:
        s = open(os.path.join(ROOT, f), encoding='utf-8').read()
        urls |= set(re.findall(r'https://template\.aksisoft\.web\.id/[^\s"\']+\.jpg', s))
    for dp, dn, fn in os.walk(os.path.join(ROOT, '_ebooks')):
        for f in fn:
            if f.endswith('.md'):
                s = open(os.path.join(dp, f), encoding='utf-8').read()
                urls |= set(re.findall(r'https://template\.aksisoft\.web\.id/[^\s"\']+\.jpg', s))
    return sorted(urls)


def plan(url):
    for pat, folder, width, q, naming in RULES:
        m = pat.search(url)
        if m:
            return folder, width, q, f'{folder}/{naming(m)}'
    return None


def fetch(job):
    url, folder, width, q, dest = job
    dp = os.path.join(ROOT, dest)
    if os.path.exists(dp):
        return dest, os.path.getsize(dp), 'ada'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        raw = urllib.request.urlopen(req, timeout=45).read()
        im = Image.open(io.BytesIO(raw))
        im.load()
        has_alpha = im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info)
        im = im.convert('RGBA' if has_alpha else 'RGB')
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        os.makedirs(os.path.dirname(dp), exist_ok=True)
        if APPLY:
            im.save(dp, 'WEBP', quality=q, method=6, exact=True)
            return dest, os.path.getsize(dp), 'baru'
        return dest, len(raw), 'rencana'
    except Exception as e:
        return dest, 0, f'GAGAL {type(e).__name__}: {str(e)[:40]}'


def main():
    jobs = []
    skipped = 0
    for u in gather():
        p = plan(u)
        if not p:
            skipped += 1
            continue
        folder, width, q, dest = p
        jobs.append((u, folder, width, q, dest))

    print(f'{len(jobs)} gambar remote akan dilokalkan ({skipped} tidak cocok pola)')
    with ThreadPoolExecutor(max_workers=8) as ex:
        res = list(ex.map(fetch, jobs))

    fail = [r for r in res if r[2].startswith('GAGAL')]
    total_new = sum(r[1] for r in res if r[2] in ('baru', 'ada'))
    for dest, kb, st in res:
        if st.startswith('GAGAL'):
            print('  ', st, dest)
    print(f'Sukses: {len(res)-len(fail)} | Gagal: {len(fail)} | Total lokal: {total_new/1048576:.1f} MB')
    if not APPLY:
        print('\nDRY-RUN. Tambahkan --apply.')
        return

    # ---- tulis ulang referensi ------------------------------------------------
    mapping = {}
    for u, folder, width, q, dest in jobs:
        if os.path.exists(os.path.join(ROOT, dest)):
            mapping[u] = '/' + dest
    n = 0
    for f in ['_data/websites.json', '_data/ebooks.json']:
        p = os.path.join(ROOT, f)
        s = open(p, encoding='utf-8').read()
        for remote, local in mapping.items():
            s = s.replace(remote, local)
        open(p, 'w', encoding='utf-8').write(s)
        n += 1
    for dp, dn, fn in os.walk(os.path.join(ROOT, '_ebooks')):
        for f in fn:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            s = open(p, encoding='utf-8').read()
            for remote, local in mapping.items():
                s = s.replace(remote, local)
            open(p, 'w', encoding='utf-8').write(s)
            n += 1
    print(f'Referensi diperbarui di {n} file')


if __name__ == '__main__':
    main()
