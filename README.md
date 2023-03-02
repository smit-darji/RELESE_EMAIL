# RELESE_EMAIL




body: |
  Hello,

  Here are the latest releases for RELESE_EMAIL:

  {% for release in releases %}
  - {{ release.name }} - {{ release.tag }}
    {{ release.body }}
    {{ release.url }}

  {% endfor %}

  Thanks,
  ChatGPT