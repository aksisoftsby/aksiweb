<#
  convert-muslimhub-poster.ps1
  Konversi screenshot/poster MuslimHub (PNG) menjadi aset web JPG untuk aksiweb:
    - assets/img/products/muslimhub-poster.jpg  -> hero visual + figure halaman /produk/muslimhub/
    - assets/img/products/muslimhub-og.jpg      -> 1200x630 untuk og:image (Facebook/WhatsApp)

  Cara pakai (dari root repo):
    powershell -ExecutionPolicy Bypass -File .\convert-muslimhub-poster.ps1

  Ganti file sumber bila perlu:
    powershell -ExecutionPolicy Bypass -File .\convert-muslimhub-poster.ps1 -Source "C:\path\poster.png"
#>
param(
  [string]$Source = (Join-Path $env:USERPROFILE 'Downloads\ChatGPT Image Sep 23, 2026, 01_13_47 PM.png')
)

Add-Type -AssemblyName System.Drawing

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$outDir = Join-Path $root 'assets\img\products'
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

# Fallback: pakai berkas "ChatGPT Image*.png" terbaru di folder Downloads.
if (-not (Test-Path $Source)) {
  $candidate = Get-ChildItem -Path (Join-Path $env:USERPROFILE 'Downloads') -Filter 'ChatGPT Image*.png' -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if ($candidate) { $Source = $candidate.FullName }
}
if (-not (Test-Path $Source)) { throw "File sumber tidak ditemukan: $Source" }

$jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() |
  Where-Object { $_.MimeType -eq 'image/jpeg' }

function Save-Jpeg {
  param([System.Drawing.Bitmap]$Bitmap, [string]$Path)
  $parameters = New-Object System.Drawing.Imaging.EncoderParameters -ArgumentList 1
  $parameters.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter -ArgumentList ([System.Drawing.Imaging.Encoder]::Quality, [int64]90)
  $Bitmap.Save($Path, $jpegCodec, $parameters)
  $parameters.Dispose()
}

function New-Canvas {
  param([int]$Width, [int]$Height)
  $bitmap = New-Object System.Drawing.Bitmap -ArgumentList $Width, $Height
  $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
  # Latar putih: JPEG tidak mengenal transparansi (sudut membulat jadi putih, bukan hitam).
  $graphics.Clear([System.Drawing.Color]::White)
  $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
  $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
  return @($bitmap, $graphics)
}

$image = [System.Drawing.Image]::FromFile($Source)
Write-Host ("Sumber : {0} ({1}x{2} px)" -f $Source, $image.Width, $image.Height)

# 1) Poster: lebar maksimal 1200 px, proporsi asli dipertahankan.
$posterWidth = [Math]::Min(1200, $image.Width)
$posterHeight = [int][Math]::Round($image.Height * $posterWidth / $image.Width)
$poster = New-Canvas -Width $posterWidth -Height $posterHeight
$poster[1].DrawImage($image, 0, 0, $posterWidth, $posterHeight)
$poster[1].Dispose()
$posterPath = Join-Path $outDir 'muslimhub-poster.jpg'
Save-Jpeg -Bitmap $poster[0] -Path $posterPath
$poster[0].Dispose()

# 2) OG image rasio 1,91:1 (1200x630) diambil dari bagian atas poster.
$ogWidth = 1200
$ogHeight = 630
$cropHeight = [Math]::Min($image.Height, [int][Math]::Round($image.Width * $ogHeight / $ogWidth))
$og = New-Canvas -Width $ogWidth -Height $ogHeight
$sourceRect = New-Object System.Drawing.Rectangle -ArgumentList 0, 0, $image.Width, $cropHeight
$targetRect = New-Object System.Drawing.Rectangle -ArgumentList 0, 0, $ogWidth, $ogHeight
$og[1].DrawImage($image, $targetRect, $sourceRect, [System.Drawing.GraphicsUnit]::Pixel)
$og[1].Dispose()
$ogPath = Join-Path $outDir 'muslimhub-og.jpg'
Save-Jpeg -Bitmap $og[0] -Path $ogPath
$og[0].Dispose()
$image.Dispose()

Write-Host ("Simpan : {0} ({1:N0} KB)" -f $posterPath, ((Get-Item $posterPath).Length / 1KB))
Write-Host ("Simpan : {0} ({1:N0} KB)" -f $ogPath, ((Get-Item $ogPath).Length / 1KB))
Write-Host "Selesai. Lanjutkan dengan 'bundle exec jekyll build' atau push ke branch gh-pages."
