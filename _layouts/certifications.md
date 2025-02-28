---
layout: page
title: "Certifications"
permalink: /certifications/
---

## 📜 Mes Certifications

{% for post in site.posts %}
  {% if post.category == "Certifications" %}
  <div class="certification-item">
    <h3>{{ post.title }}</h3>
    <a href="{{ post.url }}">
      <img src="{{ post.img }}" alt="{{ post.title }}" style="max-width: 300px; height: auto;">
    </a>
    <p><a href="{{ post.url }}">Voir les détails</a></p>
  </div>
  {% endif %}
{% endfor %}
