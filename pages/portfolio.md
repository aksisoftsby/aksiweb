---
layout: portfolio
title: Portfolio Projects
description: Koleksi proyek terbaik yang telah kami selesaikan untuk klien-klien kami.
eyebrow: Hasil Karya
---

<div class="section-head">
  <div>
    <p class="eyebrow">{{ page.eyebrow }}</p>
    <h1>{{ page.title }}</h1>
    {% if page.description %}<p>{{ page.description }}</p>{% endif %}
  </div>
</div>

<div class="grid cards portfolio-grid">
  {% assign sorted_projects = site.portfolio | sort: 'order' %}
  {% for project in sorted_projects %}
    <article class="portfolio-card">
      {% if project.image %}
        <div class="portfolio-thumb" style="background-image: url('{{ project.image }}');"></div>
      {% else %}
        <div class="portfolio-thumb placeholder">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <rect x="3" y="3" width="18" height="18" rx="2"/>
            <circle cx="8.5" cy="8.5" r="1.5"/>
            <path d="M21 15l-5-5L5 21"/>
          </svg>
        </div>
      {% endif %}
      <div class="portfolio-content">
        <span class="portfolio-category">{{ project.category }}</span>
        <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
        <p>{{ project.description }}</p>
        <a href="{{ project.url | relative_url }}" class="read-more">Lihat Detail →</a>
      </div>
    </article>
  {% endfor %}
</div>

<div class="section" style="text-align: center; margin-top: 60px;">
  <h2>Siap Memulai Proyek Anda?</h2>
  <p>Kami siap membantu mewujudkan ide digital Anda menjadi kenyataan.</p>
  <div class="hero-actions" style="justify-content: center;">
    <a href="/kontak/" class="btn primary">Hubungi Kami Sekarang</a>
    <a href="/layanan/" class="btn">Lihat Layanan</a>
  </div>
</div>

<style>
.portfolio-grid {
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
}
.portfolio-card {
  overflow: hidden;
  padding: 0;
  display: flex;
  flex-direction: column;
}
.portfolio-thumb {
  height: 200px;
  background-size: cover;
  background-position: center;
  background-color: #e2e8f0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.portfolio-thumb.placeholder {
  color: #64748b;
}
.portfolio-thumb.placeholder svg {
  width: 48px;
  height: 48px;
  opacity: 0.5;
}
.portfolio-content {
  padding: 24px;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.portfolio-category {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--brand);
  font-weight: 700;
  margin-bottom: 8px;
  display: inline-block;
}
.portfolio-content h3 {
  margin: 0 0 10px;
  font-size: 1.25rem;
}
.portfolio-content p {
  color: var(--muted);
  font-size: 0.95rem;
  margin: 0 0 16px;
  flex: 1;
}
.portfolio-content .read-more {
  font-weight: 700;
  color: var(--brand);
  text-decoration: none;
}
@media(max-width: 760px) {
  .portfolio-grid {
    grid-template-columns: 1fr;
  }
}
</style>
