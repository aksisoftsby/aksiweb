---
layout: page
title: Portfolio Kami
description: Koleksi proyek terbaik yang telah kami selesaikan untuk klien-klien kami.
eyebrow: Hasil Karya
permalink: /portfolio/
---

<div class="grid">
  {% assign sorted_portfolio = site.portfolio | sort: 'order' %}
  {% for item in sorted_portfolio %}
  <article class="hero-card">
    <div class="eyebrow">{{ item.category }}</div>
    <h3>{{ item.title }}</h3>
    <p>{{ item.description }}</p>
    <a href="{{ item.url | relative_url }}" class="read-more">Lihat Detail →</a>
  </article>
  {% endfor %}
</div>

<div class="section" style="text-align: center; margin-top: 40px;">
  <h2>Siap Memulai Proyek Anda?</h2>
  <p>Kami siap membantu mewujudkan ide digital Anda menjadi kenyataan.</p>
  <div class="hero-actions" style="justify-content: center;">
    <a href="/kontak/" class="btn primary">Hubungi Kami Sekarang</a>
    <a href="/layanan/" class="btn">Lihat Layanan</a>
  </div>
</div>
