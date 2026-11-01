#!/usr/bin/env bash
# Generate PDF company profile dari company-profile.html (Linux).
# Pengganti scripts/build-compro-pdf.ps1 (versi Windows/Edge).
# Alur: Chrome headless render HTML -> ghostscript optimasi ukuran.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
HTML_PATH="$REPO_ROOT/company-profile.html"
PDF_DIR="$REPO_ROOT/assets/downloads"
PDF_PATH="$PDF_DIR/compro-aksisoft.pdf"
ROOT_PDF_PATH="$REPO_ROOT/compro-aksisoft.pdf"
TMP_PDF="$(mktemp /tmp/compro-XXXXXX.pdf)"

CHROME_CANDIDATES=(
  "$HOME/.cache/puppeteer/chrome"/linux-*/chrome-linux64/chrome
  /usr/bin/google-chrome
  /usr/bin/chromium
  /usr/bin/chromium-browser
)

CHROME=""
for c in "${CHROME_CANDIDATES[@]}"; do
  if [ -x "$c" ]; then CHROME="$c"; break; fi
done
if [ -z "$CHROME" ]; then
  echo "ERROR: Chrome/Chromium tidak ditemukan." >&2
  exit 1
fi

[ -f "$HTML_PATH" ] || { echo "ERROR: $HTML_PATH tidak ada" >&2; exit 1; }
mkdir -p "$PDF_DIR"

echo "Browser : $CHROME"
echo "Source  : $HTML_PATH"
"$CHROME" --headless=new --disable-gpu --no-sandbox --disable-dev-shm-usage \
  --no-pdf-header-footer --virtual-time-budget=8000 \
  --print-to-pdf="$TMP_PDF" "file://$HTML_PATH" 2>/dev/null

# Optimasi ukuran (kualitas cetak, gambar 150dpi)
if command -v gs >/dev/null 2>&1; then
  gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/printer \
     -dColorImageResolution=150 -dGrayImageResolution=150 -dMonoImageResolution=300 \
     -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$PDF_PATH" "$TMP_PDF"
else
  cp "$TMP_PDF" "$PDF_PATH"
fi
rm -f "$TMP_PDF"

cp -f "$PDF_PATH" "$ROOT_PDF_PATH"
echo "PDF generated: $(stat -c%s "$PDF_PATH" | numfmt --to=iec)B"
echo "Updated both assets/downloads/compro-aksisoft.pdf and compro-aksisoft.pdf"
