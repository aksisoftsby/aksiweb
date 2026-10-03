---
layout: page
title: Portfolio Kami
description: Koleksi proyek dan produk digital yang telah kami selesaikan untuk klien dan pengguna kami.
eyebrow: Hasil Karya
permalink: /portfolio/
---

{% assign sorted_portfolio = site.portfolio | sort: 'order' %}
<div class="portfolio-grid-2">
  {% for item in sorted_portfolio %}
  <article class="portfolio-card">
    <a class="portfolio-shot" href="{{ item.url | relative_url }}">
      {% if item.image %}
      <img src="{{ item.image | relative_url }}" alt="Screenshot {{ item.title }}" loading="{% if forloop.index <= 2 %}eager{% else %}lazy{% endif %}" decoding="async">
      {% else %}
      <span class="portfolio-shot-fallback">{{ item.title }}</span>
      {% endif %}
    </a>
    <div class="portfolio-card-body">
      <p class="eyebrow">{{ item.category }}</p>
      <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
      <p>{{ item.description }}</p>
      <div class="portfolio-card-actions">
        <a href="{{ item.url | relative_url }}" class="read-more">Lihat Detail →</a>
        {% if item.site_url %}<a href="{{ item.site_url }}" target="_blank" rel="noopener noreferrer" class="read-more">Kunjungi Situs ↗</a>{% endif %}
      </div>
    </div>
  </article>
  {% endfor %}
</div>

<div class="content-wrap" style="margin-top: 28px;">
  <h2>Produk Aksisoft</h2>
  <p>Selain proyek klien, kami membangun produk digital sendiri yang digunakan publik. Berikut rangkaiannya.</p>
  <div class="portfolio-product-grid">
    {% assign products = site.pages | where: 'layout', 'product' | sort: 'product_order' %}
    {% for product in products %}
    <article class="portfolio-card">
      <a class="portfolio-shot" href="{{ product.url | relative_url }}">
        {% if product.hero_image %}
        <img src="{{ product.hero_image | relative_url }}" alt="Screenshot {{ product.product_name }}" loading="lazy" decoding="async">
        {% else %}
        <span class="portfolio-shot-fallback">{{ product.product_name }}</span>
        {% endif %}
      </a>
      <div class="portfolio-card-body">
        <p class="eyebrow">{{ product.product_label | default: 'Produk' }}</p>
        <h3><a href="{{ product.url | relative_url }}">{{ product.product_name }}</a></h3>
        <p>{{ product.description | truncate: 130 }}</p>
        <div class="portfolio-card-actions">
          <a href="{{ product.url | relative_url }}" class="read-more">Lihat Produk →</a>
          {% if product.product_url %}<a href="{{ product.product_url }}" target="_blank" rel="noopener noreferrer" class="read-more">Kunjungi {{ product.product_domain }} ↗</a>{% endif %}
        </div>
      </div>
    </article>
    {% endfor %}
  </div>
</div>

<div class="content-wrap" style="text-align: center; margin-top: 28px;">
  <h2>Siap Memulai Proyek Anda?</h2>
  <p>Kami siap membantu mewujudkan ide digital Anda menjadi kenyataan.</p>
  <div class="hero-actions" style="justify-content: center;">
    <a href="{{ '/kontak/' | relative_url }}" class="btn btn-primary">Hubungi Kami Sekarang</a>
    <a href="{{ '/layanan/' | relative_url }}" class="btn btn-outline">Lihat Layanan</a>
  </div>
</div>
