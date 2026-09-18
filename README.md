# WU的实践笔记

内容创作、品牌建设与 AI 实践，记录实测可复用的经验。

- 网站：https://wuweilab.github.io/
- 当前维护仓库：https://github.com/wuweilab/wuweilab.github.io
- Cloudflare 地址：https://wuweilab.pages.dev/（Pages 项目：wuweilab，生产分支：main）
- 旧 Cloudflare 地址：https://ai-workshop-3z3.pages.dev/（已设置保留路径与查询参数的 301 跳转；不要向旧 ai-workshop 项目上传网站内容）

## 本地预览

在本目录运行 `python -m http.server 4175`，然后打开 http://localhost:4175/ 。无需构建。

`index.html` 包含首页和交互，`articles/` 包含文章，`assets/` 包含图片、样式和音乐。
知识树草稿仅保存在浏览器 localStorage，不会自动同步到线上。
电台现含用户提供的五首本地 MP3，使用对应专辑封面，支持单曲循环。《月光奏鸣曲》仅保留 Noble Music Project 演奏的第一乐章。原有录音文件保留但不列入歌单。

更新本仓库 main 分支后，通过 GitHub Pages 发布。

## Cloudflare 发布

每次推送 main 分支，GitHub Actions 工作流 .github/workflows/cloudflare-pages.yml 自动将网站发布到 Cloudflare Pages 项目 wuweilab 的生产分支 main。也可在 Actions 中手动运行 Deploy Cloudflare Pages。

首次使用须设置仓库 Secret CLOUDFLARE_API_TOKEN，权限为 Account / Cloudflare Pages / Edit，并限定到本项目所属账户。工作流仅上传 index.html、articles/、assets/、wisdom-ball/ 和 .nojekyll；旧项目 ai-workshop 仅承载迁移跳转。
