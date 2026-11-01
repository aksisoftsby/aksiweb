const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function generatePDF() {
    const repoRoot = __dirname;
    const htmlPath = path.join(repoRoot, 'company-profile.html');
    const pdfDir = path.join(repoRoot, 'assets', 'downloads');
    const pdfPath = path.join(pdfDir, 'compro-aksisoft.pdf');
    const rootPdfPath = path.join(repoRoot, 'compro-aksisoft.pdf');

    if (!fs.existsSync(htmlPath)) {
        throw new Error(`Source HTML not found: ${htmlPath}`);
    }

    fs.mkdirSync(pdfDir, { recursive: true });

    const htmlUri = `file://${htmlPath}`;

    console.log(`Source: ${htmlPath}`);
    console.log(`Output: ${pdfPath}`);

    const browser = await puppeteer.launch({
        headless: 'new',
        args: [
            '--disable-gpu',
            '--no-first-run',
            '--disable-extensions',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--virtual-time-budget=10000'
        ]
    });

    const page = await browser.newPage();
    
    // Set viewport for A4
    await page.setViewport({ width: 794, height: 1123, deviceScaleFactor: 2 });

    // Listen for console messages
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', err => console.error('PAGE ERROR:', err.message));

    await page.goto(htmlUri, { waitUntil: 'networkidle0', timeout: 60000 });

    // Wait for fonts and images to load
    await new Promise(resolve => setTimeout(resolve, 5000));

    // Check if page is still open
    if (page.isClosed()) {
        throw new Error('Page closed unexpectedly');
    }

    // Generate PDF with page's own print CSS
    await page.pdf({
        path: pdfPath,
        format: 'A4',
        printBackground: true,
        displayHeaderFooter: false,
        margin: { top: 0, right: 0, bottom: 0, left: 0 },
        preferCSSPageSize: true
    });

    await browser.close();

    // Verify PDF
    const stats = fs.statSync(pdfPath);
    if (stats.size < 100000) {
        throw new Error(`Generated PDF looks incomplete (${stats.size} bytes)`);
    }

    // Copy to root
    fs.copyFileSync(pdfPath, rootPdfPath);

    console.log(`PDF generated: ${stats.size.toLocaleString()} bytes`);
    console.log('Updated both assets/downloads/compro-aksisoft.pdf and compro-aksisoft.pdf');
}

generatePDF().catch(err => {
    console.error('Error:', err.message);
    process.exit(1);
});