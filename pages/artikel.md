---
layout: page
title: Artikel SEO Jasa Digital per Kota
description: "Kumpulan halaman layanan Aksisoft untuk kota-kota besar di Jawa dan Bali, mulai dari jasa buat website, aplikasi Android, aplikasi custom, sampai website murah."
eyebrow: Artikel & Kata Kunci
permalink: /artikel/
---

<p class="page-intro">
  Halaman di bawah adalah landing page per kata kunci dan per kota, bukan berita.
  Semua halaman menjelaskan layanan yang kami kerjakan di wilayah Jawa dan Bali,
  lengkap dengan estimasi cara kerja, dan cara memesannya.
</p>

{% assign by_keyword = site.seo_articles | group_exp: "item", "item.service_label" %}

{% for group in by_keyword %}
  {% assign sorted = group.items | sort: "city" %}
  <section class="seo-hub-group">
    <h2>{{ group.name }}</h2>
    <p class="seo-hub-note">{{ sorted.size }} halaman tersedia untuk wilayah berikut.</p>
    <ul class="seo-hub-list">
      {% for item in sorted %}
      <li>
        <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
        <span class="seo-hub-city">{{ item.city }}{% if item.province %}, {{ item.province }}{% endif %}</span>
      </li>
      {% endfor %}
    </ul>
  </section>
{% endfor %}

<section class="seo-hub-cta">
  <h2>Belum menemukan kota Anda?</h2>
  <p>
    Kami tetap menerima proyek di luar daftar di atas, termasuk wilayah Bali lainnya
    seperti Badung, Gianyar, Tabanan, Jembrana, Buleleng, Karangasem, Bangli, dan Klungkung.
    Sampaikan saja kebutuhan Anda.
  </p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="{{ '/kontak/' | relative_url }}">Konsultasi Gratis</a>
    <a class="btn btn-outline" href="{{ '/layanan/' | relative_url }}">Lihat Layanan</a>
  </div>
</section>