---
layout: page
title: 博客
---
<div class="section-title"><span class="bar"></span>📝 全部文章</div>
<p class="section-subtitle">共 {{ site.posts.size }} 篇</p>

<ul class="post-list">
  {% for post in site.posts %}
  <li class="post-item">
    <div class="post-meta">
      <span>📅 {{ post.date | date: "%Y-%m-%d" }}</span>
      {% if post.categories %}
      <span>🗂 {{ post.categories | join: ' / ' }}</span>
      {% endif %}
    </div>
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <div class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 40 }}</div>
    {% if post.tags %}
    <div class="post-tags">
      {% for tag in post.tags %}
      <span class="tag">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </li>
  {% endfor %}
</ul>