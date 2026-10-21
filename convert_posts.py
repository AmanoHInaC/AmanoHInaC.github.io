#!/usr/bin/env python3
"""将 _posts/*.md 转换为 posts/*.html 文章页"""
import re, os, datetime

def md_inline(t):
    # bold
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    # inline code
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t

def md_block(md):
    lines = md.split('\n')
    out = []
    i = 0
    in_fence = False
    fence_lang = ''
    buf = []
    while i < len(lines):
        line = lines[i]
        # fenced code
        if line.startswith('```'):
            if not in_fence:
                in_fence = True
                fence_lang = line[3:].strip()
                buf = []
            else:
                in_fence = False
                lang = fence_lang
                out.append(f'<pre><code class="language-{lang}">' + '\n'.join(buf).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;') + '</code></pre>')
            i += 1; continue
        if in_fence:
            buf.append(line); i += 1; continue
        # blank
        if line.strip() == '':
            i += 1; continue
        # blockquote
        if line.startswith('> '):
            q = []
            while i < len(lines) and lines[i].startswith('> '):
                q.append(md_inline(lines[i][2:].replace('「','"').replace('」','"')))
                i += 1
            out.append('<blockquote>' + '<br>'.join(q) + '</blockquote>')
            continue
        # headings
        m = re.match(r'^(#{2,3})\s+(.+)$', line)
        if m:
            lvl = '2' if len(m.group(1))==2 else '3'
            out.append(f'<h{lvl}>{md_inline(m.group(2))}</h{lvl}>')
            i += 1; continue
        # list
        if re.match(r'^\s*[-*]\s+', line):
            items = []
            while i < len(lines) and re.match(r'^\s*[-*]\s+', lines[i]):
                items.append(md_inline(re.sub(r'^\s*[-*]\s+', '', lines[i])))
                i += 1
            out.append('<ul>' + ''.join(f'<li>{it}</li>' for it in items) + '</ul>')
            continue
        # paragraph
        p = []
        while i < len(lines) and lines[i].strip() != '' and not lines[i].startswith(('#','```','> ','- ')):
            p.append(md_inline(lines[i])); i += 1
        out.append('<p>' + ' '.join(p) + '</p>')
    return '\n'.join(out)

def render_page(title, date, tags, body_md):
    body = md_block(body_md)
    tags_html = ''.join(f'<span class="tag">{t}</span>' for t in tags)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} · AmanoHInaC</title>
  <link rel="icon" href="https://github.com/amanohinac.png" type="image/png">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
  <nav class="nav">
    <a href="../index.html" class="brand"><span class="dot"></span>AmanoHInaC</a>
    <div class="nav-links"><a href="../index.html">首页</a><a href="../index.html#posts">文章</a><a href="../about.html">关于</a></div>
  </nav>
  <div class="wrap">
    <header class="article-head">
      <a class="back-link" href="../index.html">← 返回首页</a>
      <h1>{title}</h1>
      <div class="meta"><span class="date">📅 {date}</span>{tags_html and '<span>🏷 </span>' or ''}{tags_html}</div>
    </header>
    <article class="article-body">
      <div class="prose">
        {body}
      </div>
    </article>
  </div>
  <footer><div>© 2024 AmanoHInaC · 用 <span class="heart">♥</span> 与星光书写</div><div style="margin-top:6px; font-size:.82rem;">托管于 GitHub Pages · <a href="../about.html">关于</a></div></footer>
</body>
</html>
"""

apps = {
    '2024-01-15-hello-world.md': {
        'out': '2024-01-15-hello-world.html',
    },
    '2024-02-10-build-your-blog.md': {
        'out': '2024-02-10-build-your-blog.html',
    },
    '2024-03-25-year-review.md': {
        'out': '2024-03-25-year-review.html',
    },
}

os.makedirs('posts', exist_ok=True)
for mdname, cfg in apps.items():
    txt = open(os.path.join('_posts', mdname), encoding='utf-8').read()
    fm, body = txt.split('---', 2)[1], txt.split('---', 2)[2]
    title = re.search(r'title:\s*["\']?(.+?)["\']?\n', fm)
    title = title.group(1) if title else '未命名'
    date = mdname[:10]
    tagm = re.search(r'tags:\s*\[(.+?)\]', fm)
    tags = [t.strip() for t in tagm.group(1).split(',')] if tagm else []
    html = render_page(title, date, tags, body.strip())
    open(os.path.join('posts', cfg['out']), 'w', encoding='utf-8').write(html)
    print(f"✓ {cfg['out']}  ({title})")

print('完成')