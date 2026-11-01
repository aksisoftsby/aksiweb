#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
localize-template-shots.py — Galeri halaman detail template (/website/<slug>/)
aselinya menunjuk 2.081 JPG remote @1920px (~230 MB) dan tiap halaman memuat
sekitar 53 gambar remote (~6 MB). Skrip ini:

  1. memilih sebagian kecil screenshot yang benar-benar ditampilkan
     (8 desktop, 4 mobile, 2 kode per template),
  2. mengunduhnya lalu menyimpan sebagai WebP seukuran render desain
     (desktop/kode 1080px, mobile 640px),
  3. menulis indeksnya ke _data/templatedims.json.

Penting: berkas ini TIDAK menyentuh _data/websites.json maupun _websites/*.md,
katalog tersebut tetap jadi hasil generate.js (URL remote). Yang dibaca layout
hanya _data/templatedims.json, jadi hasil generate ulang tidak merusak galeri.

    python3 scripts/localize-template-shots.py            # lihat rencana
    python3 scripts/localize-template-shots.py --apply     # unduh + tulis indeks
"""
import os, re, sys, json, io, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = '--apply' in sys.argv
UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120 Safari/537.36')

# jenis -> (jumlah diambil, lebar target, kualitas)
KINDS = {
    'desktop': (8, 1080, 72),
    'mobile':  (4, 640, 72),
    'code':    (2, 1080, 68),
}
OUT_DIR = 'assets/img/templates'


def remote_urls(gallery):
    """Terima dict / JSON-string, kembalikan {jenis: [url]}."""
    if isinstance(gallery, str):
        try:
            gallery = json.loads(gallery)
        except Exception:
            return {}
    if not isinstance(gallery, dict):
        return {}
    return {k: [u for u in (v or []) if isinstance(u, str)] for k, v in gallery.items()}


def jobs_from(data):
    jobs, index, order, seen = [], {}, [], set()
    stem_pat = re.compile(r'screenshot-([a-z0-9-]+)\.jpg$', re.I)
    for it in data:
        slug = it.get('slug')
        if not slug:
            continue
        gal = remote_urls(it.get('gallery'))
        index[slug] = {'shots': {}, 'dims': {}}
        for kind, (limit, width, q) in KINDS.items():
            urls, names = [], []
            for u in gal.get(kind, [])[:limit]:
                m = stem_pat.search(u)
                stem = (m.group(1) if m else str(len(urls) + 1)).replace('-', '_')
                urls.append(u)
                names.append(f'{kind}-{stem}')
            for u, nm in zip(urls, names):
                # URL galeri yang ternyata sudah menunjuk file lokal
                # (thumbnail katalog) dipakai apa adanya, tidak perlu diunduh.
                if u.startswith('/assets/'):
                    order.append((slug, kind, u))
                    continue
                if not u.startswith('http'):
                    continue
                dest = f'{OUT_DIR}/{slug}/{nm}.webp'
                if dest in seen:
                    continue
                seen.add(dest)
                jobs.append((u, dest, width, q, slug))
                order.append((slug, kind, '/' + dest))
        # sampul halaman demo utama = thumbnail katalog yang sudah lokal
        thumb = it.get('thumbnail') or ''
        if thumb.startswith('/assets/'):
            order.append((slug, 'thumb', thumb))
        for slug2, kind, key in order:
            index[slug2]['dims'].setdefault(key, {'w': None, 'h': None})
    return jobs, index, order


def run(job):
    url, dest, width, q, slug = job
    dp = os.path.join(ROOT, dest)
    if os.path.exists(dp):
        return slug, dest, Image.open(dp).size, 'sudah ada'
    try:
        raw = urllib.request.urlopen(
            urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read()
        im = Image.open(io.BytesIO(raw))
        im.load()
        im = im.convert('RGB')
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        if APPLY:
            os.makedirs(os.path.dirname(dp), exist_ok=True)
            im.save(dp, 'WEBP', quality=q, method=6)
        return slug, dest, im.size, 'ok'
    except Exception as e:
        return slug, dest, None, f'GAGAL {type(e).__name__}: {str(e)[:50]}'


def main():
    data = json.load(open(os.path.join(ROOT, '_data', 'websites.json'), encoding='utf-8'))
    jobs, index, order = jobs_from(data)
    print(f'{len(jobs)} screenshot terpilih dari {len(index)} template')

    with ThreadPoolExecutor(max_workers=8) as ex:
        res = list(ex.map(run, jobs))

    fails = [(s, d, st) for s, d, sz, st in res if st.startswith('GAGAL')]
    for s, d, st in fails[:12]:
        print('  ', st, d)

    # susun shots + dimensi berdasarkan file yang benar-benar ada
    for slug in list(index):
        index[slug] = {'shots': {}, 'dims': {}}
    kb = 0
    for slug, kind, key in order:
        p = os.path.join(ROOT, key.lstrip('/'))
        if not os.path.exists(p):
            continue
        lst = index[slug]['shots'].setdefault(kind, [])
        if key in lst:
            continue
        with Image.open(p) as im:
            size = im.size
        lst.append(key)
        index[slug]['dims'][key] = {'w': size[0], 'h': size[1]}
        kb += os.path.getsize(p)
    # gambar halaman utama demo tampil paling dulu
    for slug, e in index.items():
        for kind in e['shots']:
            e['shots'][kind].sort(key=lambda k: 0 if k.endswith(f'{kind}-index.webp') else 1)
    for s in [s for s, v in index.items() if not v['shots'].get('desktop')]:
        index.pop(s)

    print(f'Terindeks {len(index)} template | '
          f'gagal unduh {len(fails)} | berat lokal {kb/1048576:.1f} MB')

    if not APPLY:
        print('\nDRY-RUN. Tambahkan --apply.')
        return

    out = os.path.join(ROOT, '_data', 'templatedims.json')
    json.dump(index, open(out, 'w', encoding='utf-8'), indent=0, sort_keys=True)
    print(f'Indeks ditulis: _data/templatedims.json ({len(index)} template)')


if __name__ == '__main__':
    main()
