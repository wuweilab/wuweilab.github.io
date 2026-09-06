# WU的实践笔记

内容创作、品牌建设与 AI 实践，记录实测可复用的经验。

- 网站：https://wuweilab.github.io/
- 当前维护仓库：https://github.com/wuweilab/wuweilab.github.io
- 原 Cloudflare 地址：https://ai-workshop-3z3.pages.dev/

## 本地预览

在本目录运行 `python -m http.server 4175`，然后打开 http://localhost:4175/ 。无需构建。

`index.html` 包含首页和交互，`articles/` 包含文章，`assets/` 包含图片、样式和音乐。
知识树草稿仅保存在浏览器 localStorage，不会自动同步到线上。
电台现含用户提供的五首本地 MP3，使用对应专辑封面，支持单曲循环。《月光奏鸣曲》仅保留 Noble Music Project 演奏的第一乐章。原有录音文件保留但不列入歌单。

更新本仓库 main 分支后，通过 GitHub Pages 发布。
