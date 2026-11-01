$ErrorActionPreference = 'Stop'

# Generate the Aksisoft company profile PDF from the HTML source.
# The script uses Microsoft Edge or Google Chrome already installed on Windows.
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$htmlPath = Join-Path $repoRoot 'company-profile.html'
$pdfDir = Join-Path $repoRoot 'assets\downloads'
$pdfPath = Join-Path $pdfDir 'compro-aksisoft.pdf'
$rootPdfPath = Join-Path $repoRoot 'compro-aksisoft.pdf'

if (-not (Test-Path $htmlPath)) {
    throw "Source HTML not found: $htmlPath"
}
New-Item -ItemType Directory -Force -Path $pdfDir | Out-Null

$browserCandidates = @(
    (Join-Path $env:ProgramFiles 'Microsoft\Edge\Application\msedge.exe'),
    (Join-Path ${env:ProgramFiles(x86)} 'Microsoft\Edge\Application\msedge.exe'),
    (Join-Path $env:ProgramFiles 'Google\Chrome\Application\chrome.exe'),
    (Join-Path ${env:ProgramFiles(x86)} 'Google\Chrome\Application\chrome.exe'),
    (Join-Path $env:LOCALAPPDATA 'Google\Chrome\Application\chrome.exe')
) | Where-Object { $_ -and (Test-Path $_) }

if (-not $browserCandidates) {
    throw 'Microsoft Edge or Google Chrome was not found. Install either browser, then run this script again.'
}
$browser = $browserCandidates[0]
$htmlUri = ([System.Uri]$htmlPath).AbsoluteUri

# Use the page's own A4 and print CSS. Local assets remain next to the HTML source.
$chromeArgs = @(
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    '--disable-extensions',
    '--no-pdf-header-footer',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=5000',
    "--print-to-pdf=$pdfPath",
    $htmlUri
)

Write-Host "Browser : $browser"
Write-Host "Source  : $htmlPath"
Write-Host "Output  : $pdfPath"
$process = Start-Process -FilePath $browser -ArgumentList $chromeArgs -Wait -PassThru -WindowStyle Hidden

if (-not (Test-Path $pdfPath)) {
    throw "PDF generation failed (browser exit code: $($process.ExitCode))."
}
$pdf = Get-Item $pdfPath
if ($pdf.Length -lt 100000) {
    throw "Generated PDF looks incomplete ($($pdf.Length) bytes). Check the browser output."
}

Copy-Item -Force $pdfPath $rootPdfPath
Write-Host ("PDF generated: {0:N0} bytes" -f $pdf.Length)
Write-Host "Updated both assets\downloads\compro-aksisoft.pdf and compro-aksisoft.pdf"
