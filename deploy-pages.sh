#!/usr/bin/env bash
# Build situs secara LOKAL lalu deploy output statis ke branch gh-pages.
#
# Dipakai karena build Jekyll di GitHub (Actions) tidak bisa diandalkan.
# Branch `gh-pages` berisi OUTPUT build (bukan source) dan memuat .nojekyll,
# sehingga GitHub Pages hanya menyajikan file apa adanya tanpa build Jekyll.
#
# Branch `source` berisi source Jekyll tempat kamu mengedit.
#
# Pemakaian:
#   bash deploy-pages.sh
#
# Prasyarat (sekali saja): Ruby portable + Jekyll ada di ../.rubyportable
#   Lihat DEPLOY-PAGES.md untuk cara menyiapkannya.

set -euo pipefail

RUBY_DIR="$(cd "$(dirname "$0")/.." && pwd)/.rubyportable/rubyinstaller-3.3.12-1-x64"
export PATH="$RUBY_DIR/bin:$PATH"
export GEM_HOME="$RUBY_DIR/lib/ruby/gems/3.3.0"
export JEKYLL_NO_BUNDLER_REQUIRE=true

cd "$(dirname "$0")"
echo "== 1/4 build Jekyll =="
jekyll build

echo "== 2/4 bersihkan _site =="
rm -f _site/assets/videos/*.mp4        # video ada di CDN (cfcdn.aksisoft.my.id)
rm -f _site/prompt.txt
touch _site/.nojekyll                  # agar GitHub Pages tidak build Jekyll

echo "== 3/4 commit output ke gh-pages (worktree tetap di source) =="
IDX="$(pwd)/.git/deploy-index"
rm -f "$IDX"
GIT_INDEX_FILE="$IDX" git --work-tree="$(pwd)/_site" add -A
TREE="$(GIT_INDEX_FILE="$IDX" git write-tree)"
rm -f "$IDX"
COMMIT="$(git commit-tree "$TREE" -p "$(git rev-parse gh-pages)" -m "Deploy build statis $(date +%Y-%m-%d\ %H:%M)")"
git update-ref refs/heads/gh-pages "$COMMIT"
echo "   gh-pages -> $COMMIT"

echo "== 4/4 push =="
git push origin gh-pages
echo "Selesai. Tunggu ~1 menit lalu cek https://aksisoft.web.id/"