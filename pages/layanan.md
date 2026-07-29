---
layout: page
title: Layanan Kami
description: Solusi digital marketing dan pembuatan website profesional untuk bisnis Anda
eyebrow: Layanan
permalink: /layanan/
---

<style>
.service-tabs { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 30px; }
.service-tab { padding: 14px 24px; border: 2px solid var(--line); border-radius: 12px; background: var(--card); cursor: pointer; font-weight: 700; transition: all 0.3s ease; }
.service-tab:hover { border-color: var(--brand); transform: translateY(-2px); }
.service-tab.active { background: var(--brand); color: white; border-color: var(--brand); }
.service-content { display: none; animation: fadeIn 0.4s ease; }
.service-content.active { display: block; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.package-card { background: var(--card); border: 2px solid var(--line); border-radius: 16px; padding: 28px; margin-bottom: 20px; transition: all 0.3s ease; }
.package-card:hover { border-color: var(--brand); box-shadow: var(--shadow); transform: translateY(-3px); }
.package-card h4 { font-size: 1.5rem; margin: 0 0 12px; color: var(--brand); }
.package-card .price { font-size: 1.8rem; font-weight: 800; margin-bottom: 16px; color: var(--text); }
.package-card ul { list-style: none; padding: 0; margin: 0 0 20px; }
.package-card li { padding: 8px 0; border-bottom: 1px solid var(--line); }
.package-card li:last-child { border-bottom: none; }
.package-card li::before { content: "✓"; color: var(--brand); font-weight: 900; margin-right: 10px; }
.feature-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 24px; }
.feature-item { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 16px; }
.feature-item strong { display: block; margin-bottom: 6px; color: var(--brand); }
</style>

<div class="service-tabs">
  <button class="service-tab active" onclick="showService('static')">Website Static</button>
  <button class="service-tab" onclick="showService('dynamic')">Website News Dynamic</button>
  <button class="service-tab" onclick="showService('google-ads')">Google Ads</button>
  <button class="service-tab" onclick="showService('social-ads')">Social Media Ads</button>
</div>

<!-- Website Static -->
<div id="static" class="service-content active">
  <h2>Jasa Pembuatan Website Static</h2>
  <p>Website static cocok untuk landing page, company profile, dan portofolio. Cepat, aman, dan SEO-friendly.</p>
  
  <div class="package-card">
    <h4>Paket Basic</h4>
    <div class="price">Rp 1.500.000</div>
    <ul>
      <li>1 Halaman Landing Page</li>
      <li>Desain Responsive (Mobile-Friendly)</li>
      <li>Integrasi WhatsApp Button</li>
      <li>SEO Dasar</li>
      <li>Hosting Gratis 1 Tahun</li>
      <li>Revisi 2x</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="package-card">
    <h4>Paket Standard</h4>
    <div class="price">Rp 3.000.000</div>
    <ul>
      <li>3-5 Halaman (Home, About, Services, Contact)</li>
      <li>Desain Custom Premium</li>
      <li>Integrasi WhatsApp & Email Form</li>
      <li>SEO On-Page Optimization</li>
      <li>Google Maps Integration</li>
      <li>Hosting Gratis 1 Tahun + Domain .com</li>
      <li>Revisi 5x</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="package-card">
    <h4>Paket Premium</h4>
    <div class="price">Rp 5.000.000</div>
    <ul>
      <li>Unlimited Halaman</li>
      <li>Desain Exclusive Custom</li>
      <li>Multi-language Support</li>
      <li>Advanced SEO Setup</li>
      <li>Google Analytics Integration</li>
      <li>Social Media Integration</li>
      <li>Hosting Premium 1 Tahun + Domain .com</li>
      <li>Revisi Unlimited</li>
      <li>Maintenance 3 Bulan Gratis</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
</div>

<!-- Website News Dynamic -->
<div id="dynamic" class="service-content">
  <h2>Jasa Pembuatan Website News Dynamic</h2>
  <p>Website berita dinamis dengan CMS untuk manajemen konten mudah. Cocok untuk portal berita, majalah online, dan blog korporat.</p>
  
  <div class="package-card">
    <h4>Paket News Basic</h4>
    <div class="price">Rp 4.500.000</div>
    <ul>
      <li>CMS Admin Panel (Login Dashboard)</li>
      <li>Kategori & Tag Artikel</li>
      <li>Upload Gambar & Video</li>
      <li>Responsive Design</li>
      <li>Komentar System</li>
      <li>SEO Basic</li>
      <li>Hosting 1 Tahun</li>
      <li>Training Penggunaan CMS</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="package-card">
    <h4>Paket News Pro</h4>
    <div class="price">Rp 7.500.000</div>
    <ul>
      <li>CMS Multi-user (Editor, Author, Admin)</li>
      <li>Kategori Unlimited & Tag System</li>
      <li>Featured Article & Slider Homepage</li>
      <li>Video Embed (YouTube, Vimeo)</li>
      <li>Comment Moderation</li>
      <li>Advanced SEO + Sitemap</li>
      <li>Google AdSense Ready</li>
      <li>Social Share Buttons</li>
      <li>Hosting Premium 1 Tahun + Domain</li>
      <li>Training & Documentation</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="package-card">
    <h4>Paket News Enterprise</h4>
    <div class="price">Rp 12.000.000</div>
    <ul>
      <li>CMS Custom dengan Fitur Lengkap</li>
      <li>Multi-author dengan Role Management</li>
      <li>Scheduled Publishing</li>
      <li>Newsletter Subscription</li>
      <li>Analytics Dashboard</li>
      <li>AMP (Accelerated Mobile Pages)</li>
      <li>Push Notification</li>
      <li>API Integration</li>
      <li>Cloud Hosting 1 Tahun + Domain Premium</li>
      <li>Priority Support 6 Bulan</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
</div>

<!-- Google Ads -->
<div id="google-ads" class="service-content">
  <h2>Jasa Google Ads</h2>
  <p>Tingkatkan visibilitas bisnis Anda di hasil pencarian Google dengan kampanye iklan yang teroptimasi.</p>
  
  <div class="package-card">
    <h4>Paket Starter</h4>
    <div class="price">Rp 2.000.000 / bulan</div>
    <ul>
      <li>Setup 1 Kampanye Search Ads</li>
      <li>Max 10 Keywords</li>
      <li>2 Iklan Ads Copy</li>
      <li>Lokasi Target 1 Kota</li>
      <li>Weekly Report</li>
      <li>Optimasi Mingguan</li>
      <li>*Belum termasuk budget iklan</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="package-card">
    <h4>Paket Business</h4>
    <div class="price">Rp 4.000.000 / bulan</div>
    <ul>
      <li>Setup 3 Kampanye (Search + Display)</li>
      <li>Max 50 Keywords</li>
      <li>5 Iklan Ads Copy per Kampanye</li>
      <li>Lokasi Target Nasional</li>
      <li>Conversion Tracking Setup</li>
      <li>Bi-weekly Optimization</li>
      <li>Detailed Performance Report</li>
      <li>A/B Testing</li>
      <li>*Belum termasuk budget iklan</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="package-card">
    <h4>Paket Enterprise</h4>
    <div class="price">Rp 8.000.000 / bulan</div>
    <ul>
      <li>Unlimited Kampanye (Search, Display, Shopping, Video)</li>
      <li>Unlimited Keywords</li>
      <li>Advanced Ad Extensions</li>
      <li>Target Global</li>
      <li>Google Analytics 4 Integration</li>
      <li>Daily Monitoring & Optimization</li>
      <li>Custom Dashboard Reporting</li>
      <li>Remarketing Campaign</li>
      <li>Dedicated Account Manager</li>
      <li>*Belum termasuk budget iklan</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="feature-grid">
    <div class="feature-item">
      <strong>🎯 Target Tepat</strong>
      <p>Iklan muncul saat calon customer mencari produk/jasa Anda</p>
    </div>
    <div class="feature-item">
      <strong>💰 Budget Fleksibel</strong>
      <p>Anda kontrol sendiri anggaran iklan harian/bulanan</p>
    </div>
    <div class="feature-item">
      <strong>📊 Terukur</strong>
      <p>Laporan detail ROI, klik, konversi, dan performa</p>
    </div>
    <div class="feature-item">
      <strong>⚡ Hasil Cepat</strong>
      <p>Iklan langsung tampil dalam 24 jam setelah approval</p>
    </div>
  </div>
</div>

<!-- Social Media Ads -->
<div id="social-ads" class="service-content">
  <h2>Jasa Social Media Ads</h2>
  <p>Jangkau jutaan pengguna aktif di platform sosial media favorit mereka dengan iklan yang engaging.</p>
  
  <div class="package-card">
    <h4>Paket Facebook & Instagram</h4>
    <div class="price">Rp 2.500.000 / bulan</div>
    <ul>
      <li>Setup Facebook & Instagram Ads</li>
      <li>3 Variasi Creative (Gambar/Video)</li>
      <li>Target Audience Research</li>
      <li>Copywriting Iklan</li>
      <li>A/B Testing 2 Versi</li>
      <li>Weekly Performance Report</li>
      <li>Optimasi Mingguan</li>
      <li>*Belum termasuk budget iklan</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="package-card">
    <h4>Paket Multi-Platform</h4>
    <div class="price">Rp 5.000.000 / bulan</div>
    <ul>
      <li>Facebook, Instagram & TikTok Ads</li>
      <li>5 Variasi Creative per Platform</li>
      <li>Advanced Audience Targeting</li>
      <li>Professional Copywriting</li>
      <li>Video Editing Simple (untuk TikTok/Reels)</li>
      <li>Retargeting Campaign</li>
      <li>Bi-weekly Optimization</li>
      <li>Detailed Analytics Report</li>
      <li>*Belum termasuk budget iklan</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="package-card">
    <h4>Paket Premium Social</h4>
    <div class="price">Rp 10.000.000 / bulan</div>
    <ul>
      <li>All Platform (FB, IG, TikTok, LinkedIn, Twitter)</li>
      <li>Unlimited Creative Variations</li>
      <li>Professional Content Production</li>
      <li>Influencer Collaboration Support</li>
      <li>Custom Audience Building</li>
      <li>Full Funnel Strategy</li>
      <li>Daily Monitoring</li>
      <li>Monthly Strategy Meeting</li>
      <li>Dedicated Social Media Specialist</li>
      <li>*Belum termasuk budget iklan</li>
    </ul>
    <a href="/kontak/" class="btn primary">Pilih Paket</a>
  </div>
  
  <div class="feature-grid">
    <div class="feature-item">
      <strong>📱 Multi Platform</strong>
      <p>Facebook, Instagram, TikTok, LinkedIn, Twitter</p>
    </div>
    <div class="feature-item">
      <strong>🎨 Creative Content</strong>
      <p>Desain visual menarik dan copywriting persuasif</p>
    </div>
    <div class="feature-item">
      <strong>👥 Precise Targeting</strong>
      <p>Target berdasarkan demografi, minat, perilaku</p>
    </div>
    <div class="feature-item">
      <strong>🔄 Retargeting</strong>
      <p>Iklan ulang untuk pengunjung website Anda</p>
    </div>
  </div>
</div>

<script>
function showService(serviceId) {
  // Hide all service content
  document.querySelectorAll('.service-content').forEach(function(content) {
    content.classList.remove('active');
  });
  
  // Remove active class from all tabs
  document.querySelectorAll('.service-tab').forEach(function(tab) {
    tab.classList.remove('active');
  });
  
  // Show selected service content
  document.getElementById(serviceId).classList.add('active');
  
  // Add active class to clicked tab
  event.target.classList.add('active');
}
</script>
