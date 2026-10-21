# AmanoHInaC 的个人博客 ✨

在星光与樱花下，用心记录美好。基于**纯 HTML / CSS / JS** 的手写静态博客，无需构建，托管于 **GitHub Pages**。

🔗 **在线访问：** <https://amanohinac.github.io>

## ✨ 特点

- 🎨 **高质感浪漫主题**：深空蓝紫渐变 + 明亮粉紫强调，毛玻璃卡片，克制的星空微动效
- ⚡ **极速加载**：纯静态页面，无任何框架与依赖，一次请求即渲染
- 🎚 **零构建**：不需要 Ruby / Jekyll，push 即生效
- 📱 **响应式**：完美适配桌面与移动端
- ♿️ **无障碍**：尊重系统「减少动态效果」偏好

## 📁 项目结构

```
├── index.html              # 首页（Hero + 文章卡片）
├── about.html              # 关于我
├── posts/                  # 独立文章页（纯 HTML）
├── assets/css/style.css    # 全部样式
└── convert_posts.py        # 工具：Markdown → HTML 文章页
```

## ✍️ 如何发布新文章

1. 用 Markdown 写文章，保存为 `_posts/年-月-日-标题.md`
2. 运行转换工具生成 HTML：
   ```bash
   python3 convert_posts.py
   ```
3. 在 `index.html` 的 `.post-grid` 里加一张文章卡片
4. 提交并推送即可：
   ```bash
   git add .
   git commit -m "发布新文章"
   git push
   ```

> 💡 现在整个站点就靠这几个文件，维护起来非常轻量可控。

---

© 2024 AmanoHInaC · Made with ♥