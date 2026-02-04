# 发布到 GitHub

## 准备工作

项目已准备好发布到 GitHub，包含以下文件：

### 必需文件
- ✅ `README.md` - 项目说明（英文）
- ✅ `README.zh.md` - 项目说明（中文）
- ✅ `LICENSE` - MIT 许可证
- ✅ `pyproject.toml` - 项目配置
- ✅ `.gitignore` - Git 忽略文件
- ✅ `.github/workflows/test.yml` - CI/CD 配置

### 文档
- ✅ `mkdocs.yml` - MkDocs 配置（支持 i18n）
- ✅ `docs/` - 完整文档目录（英文）
- ✅ `docs/zh/` - 中文文档目录

### 测试
- ✅ `tests/` - 完整测试套件

## 发布步骤

### 1. 创建 GitHub 仓库

1. 访问 [GitHub](https://github.com/new)
2. 填写仓库信息：
   - Repository name: `knowai-sse`
   - Description: Semantic Seed Expander
   - Public/Private: Public
   - License: MIT
3. 点击 "Create repository"

### 2. 推送代码

```bash
cd /home/tobegold574/knowai/V1/awake/knowai-sse
git init
git add .
git commit -m "Initial release: v0.1.0"
git branch -M main
git remote add origin https://github.com/your-username/knowai-sse.git
git push -u origin main
```

### 3. 启用 GitHub Actions

推送后，GitHub Actions 会自动运行测试。检查：
- Actions 标签页
- 确认测试通过

### 4. 启用 GitHub Pages

1. 进入仓库的 Settings > Pages
2. Source 选择 "GitHub Actions"
3. 保存后，文档将自动部署

### 5. 发布到 PyPI (可选)

如果需要发布到 PyPI：

```bash
pip install build twine
python -m build
twine upload dist/*
```

## MkDocs 使用指南

### 安装依赖

```bash
pip install mkdocs-material mkdocs-i18n
```

### 本地预览文档

```bash
cd /home/tobegold574/knowai/V1/awake/knowai-sse
mkdocs serve
```

访问 http://127.0.0.1:8000 查看文档

### 构建文档

```bash
mkdocs build
```

构建后的文件在 `site/` 目录，包含：
- `/` - 英文文档
- `/zh/` - 中文文档

### 部署到 GitHub Pages

文档会通过 GitHub Actions 自动部署，当以下文件变更时触发：
- `docs/**` - 文档内容
- `mkdocs.yml` - 配置文件
- `.github/workflows/deploy-docs.yml` - 部署工作流

### 文档结构

```
docs/
├── index.md              # 英文首页
├── guide/                # 英文用户指南
│   ├── installation.md
│   ├── quickstart.md
│   └── concepts.md
├── api/                  # 英文 API 参考
│   ├── expander.md
│   ├── prompt_mgr.md
│   ├── llm_client.md
│   └── models.md
├── dev/                  # 英文开发者指南
│   ├── testing.md
│   └── contributing.md
└── zh/                   # 中文文档
    ├── index.md
    ├── guide/
    ├── api/
    └── dev/
```

### 多语言配置

MkDocs 已配置 i18n 插件，支持：
- 英文（默认）：`/`
- 中文：`/zh/`

文档页面顶部会显示语言切换按钮。

## 后续维护

### 发布新版本

1. 更新 `pyproject.toml` 中的版本号
2. 更新 `CHANGELOG.md`
3. 创建 Git tag：
   ```bash
   git tag v0.2.0
   git push origin v0.2.0
   ```

### 更新文档

修改 `docs/` 下的文件后：
- 推送到 main 分支会自动触发文档部署
- 英文和中文文档需要分别更新

### 同步中英文文档

当更新文档时，确保：
1. 更新 `docs/` 下的英文文件
2. 同步更新 `docs/zh/` 下的中文文件
3. 推送代码触发自动部署

## 注意事项

- 确保 `tests/.env` 不会被提交（已在 `.gitignore` 中）
- GitHub Actions 会在每次推送时自动运行测试
- 文档更新后会自动部署到 GitHub Pages
- 中英文文档需要分别维护和更新
