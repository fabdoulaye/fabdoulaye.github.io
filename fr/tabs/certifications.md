---
layout: page
title: "Mes Certifications"
permalink: /certifications/
---

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.css" />
<script src="https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.js"></script>

## 📜 Mes Certifications

<div class="swiper-container">
  <div class="swiper-wrapper">
    {% for cert in site.data.certifications %}
    <div class="swiper-slide">
      <a href="{{ cert.link }}" target="_blank">
        <img src="{{ cert.image }}" alt="{{ cert.title }}" style="max-width: 100%; height: auto;">
      </a>
      <p>{{ cert.title }} - {{ cert.organization }}</p>
    </div>
    {% endfor %}
  </div>
  
  <!-- Boutons de navigation -->
  <div class="swiper-button-next"></div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-pagination"></div>
</div>

<script>
  var swiper = new Swiper('.swiper-container', {
    loop: true,
    pagination: { el: '.swiper-pagination', clickable: true },
    navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
  });
</script>
