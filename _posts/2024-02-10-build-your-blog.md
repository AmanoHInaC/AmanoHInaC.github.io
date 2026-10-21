---
layout: post
title: "如何搭建一个属于自己的技术博客"
date: 2024-02-10 10:00:00 +0800
categories: [技术, 建站]
tags: [Jekyll, GitHub Pages, 教程]
---

拥有一块属于自己的网络空间，是一件很酷的事情。今天就来分享如何快速搭建一个个人技术博客。

## 方案对比

搭建个人博客主要有以下几种方案：

| 方案 | 优点 | 缺点 |
|------|------|------|
| GitHub Pages + Jekyll | 免费、无需服务器、支持自定义域名 | 构建速度一般 |
| Vercel/Netlify | 部署快、支持多种框架 | 托管在海外 |
| 自建服务器 | 完全可控 | 需要维护、成本高 |

对于大多数朋友，**GitHub Pages + Jekyll** 是最省心的选择，因为它免费、稳定，而且本博客正是基于此构建。

## 核心步骤

### 1. 创建仓库

在 GitHub 上创建一个名为 `<你的用户名>.github.io` 的仓库。

### 2. 克隆到本地

```bash
git clone https://github.com/<用户名>/<用户名>.github.io.git
```

### 3. 配置站点

编辑 `_config.yml`，设置标题、作者、描述等基本信息。

### 4. 写文章

在 `_posts` 目录下以 `年-月-日-标题.md` 命名创建 Markdown 文件：

```markdown
---
layout: post
title: "文章标题"
date: 2024-02-10
categories: [技术]
tags: [标签]
---

这里是正文……
```

### 5. 推送上线

```bash
git add .
git commit -m "发布新文章"
git push origin main
```

推送到 GitHub 后，Pages 会自动构建，稍等一会儿就能在 `https://<用户名>.github.io` 访问了。

## 小结

搭建博客并不难，难的是坚持下去的写作热情。祝你在写作的路上越走越远！

> 💡 小提示：保持「随手记录」的习惯，灵感稍纵即逝。少即是多，贵在坚持。