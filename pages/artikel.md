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
  lengkap dengan estimasi biaya, cara kerja, dan cara memesannya.
</p>

{% assign layanan_list = "Jasa Pembuatan Website|Jasa Aplikasi Android|Jasa Aplikasi Custom|Jasa Website Murah|Jasa Website Company Profile|Jasa Landing Page|Jasa Toko Online|Jasa SEO Lokal|Jasa Redesign Website|Jasa Sistem Custom dan Integrasi" | split: "|" %}
{% assign total_halaman = site.seo_articles.size %}

{% for label in layanan_list %}
  {% assign items = site.seo_articles | where: "service_label", label %}
  {% if items.size > 0 %}
    {% assign sorted = items | sort: "city" %}
  <section class="seo-hub-group">
    <h2>{{ label }}</h2>
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
  {% endif %}
{% endfor %}

{% assign jumlah_kota = site.seo_articles | map: "city" | uniq %}

<section class="seo-hub-cta">
  <h2>Ringkasan dan kota berikutnya</h2>
  <p>
    Total <strong>{{ total_halaman }}</strong> halaman layanan untuk
    <strong>{{ jumlah_kota.size }}</strong> kota di Jawa dan Bali. Daftar kota saat ini:
    {{ jumlah_kota | join: ', ' }}.
  </p>
  <p>
    Kami tetap menerima proyek di luar daftar tersebut, termasuk wilayah Bali lainnya
    seperti Badung, Gianyar, Tabanan, Jembrana, Buleleng, Karangasem, Bangli, dan Klungkung.
    Sampaikan saja kebutuhan Anda.
  </p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="{{ '/kontak/' | relative_url }}">Konsultasi Gratis</a>
    <a class="btn btn-outline" href="{{ '/layanan/' | relative_url }}">Lihat Layanan</a>
  </div>
</section>