---
layout: page
title: "Mes Certifications"
permalink: /certifications/
To get my certifications files, you need to create a `_data` folder in the root of your repository and add a `certifications.yml` file inside it. The `certifications.yml` file should contain your certifications data in the following format:

```yaml
- title: "Certification Title 1"
    organization: "Organization Name 1"
    link: "/certifications/Certification1.pdf"
    image: "https://example.com/image1.jpg"

- title: "Certification Title 2"
    organization: "Organization Name 2"
    link: "/certifications/Certification2.pdf"
    image: "https://example.com/image2.jpg"

# Add more certifications as needed
```

Make sure to place your PDF files in the `certifications` folder in your repository.

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.css" />
<script src="https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.js"></script>

## 📜 Mes Certifications


{% for post in site.posts %}
  {% if post.category == "Certifications" %}
  <div>
    <h3>{{ post.title }}</h3>
    <a href="{{ post.url }}">
      <img src="{{ post.img }}" alt="{{ post.title }}" style="max-width: 300px; height: auto;">
    </a>
    <p><a href="{{ post.url }}">Voir les détails</a></p>
  </div>
  {% endif %}
{% endfor %}


