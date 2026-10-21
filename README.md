# AmanoHInaC 的个人博客 ✨

基于 **Jekyll + GitHub Pages** 的个人博客站点，免费、静态、响应式，带有一套自研的精美深色主题。

🔗 **在线访问：** <https://amanohinac.github.io>

## ✨ 特性

- 🎨 自研精美深色渐变主题，毛玻璃卡片、渐变文字、响应式布局
- 📝 纯 Markdown 写作，简单易用
- 🚀 GitHub Pages 免费托管，push 即发布
- 📱 完美适配桌面端与移动端
- 🔎 内置 SEO 与站点地图

## 🏗️ 技术栈

| 组件 | 说明 |
|------|------|
| Jekyll | 静态站点生成器 |
| GitHub Pages | 免费托管 & 自动构建 |
| Sass | 样式预处理 |
| Markdown | 文章写作格式 |

## 📝 发布一篇文章

在 `_posts/` 目录下新建一个文件，命名为 `年-月-日-标题.md`，格式如下：

```markdown
---
layout: post
title: "文章标题"
date: 2024-05-01 10:00:00 +0800
categories: [技术]
tags: [标签1, 标签2]
---

这里是文章正文……
```

然后提交推送即可：

```bash
git add _posts/新文件.md
git commit -m "发布新文章"
git push origin main
```

## 🔧 本地预览（可选）

```bash
# 需要 Ruby 环境
gem install bundler jekyll
bundle install
bundle exec jekyll serve
```

然后访问 <http://localhost:4000>。

## 📄 站点结构

```
├── _layouts/          # 页面模板
├── _includes/         # 公共组件（导航、页脚）
├── _posts/            # 文章（Markdown）
├── _sass/             # Sass 样式模块
├── assets/css/        # 编译后的样式
├── index.html         # 首页
├── blog.md            # 全部文章列表
├── about.md           # 关于我
└── _config.yml        # 站点配置
```

## 📄 许可证

本项目 MIT 许可。欢迎使用与改造。图片与内容版权归作者所有。

---

© {:.no_toc} 2024 AmanoHInaC · Made with ❤️