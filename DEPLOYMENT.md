# 发布到 GitHub

## 准备工作

项目已准备好发布到 GitHub，包含以下文件：

### 必需文件
- ✅ `README.md` - 项目说明
- ✅ `LICENSE` - MIT 许可证
- ✅ `pyproject.toml` - 项目配置
- ✅ `.gitignore` - Git 忽略文件
- ✅ `.github/workflows/test.yml` - CI/CD 配置

### 文档
- ✅ `mkdocs.yml` - MkDocs 配置
- ✅ `docs/` - 完整文档目录

### 测试
- ✅ `tests/` - 完整测试套件

## 发布步骤

### 1. 创建 GitHub 仓库

1. 访问 [GitHub](https://github.com/new)
2. 填写仓库信息：
   - Repository name: `knowai-sse`
   - Description: 语义种子扩展引擎
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

### 4. 发布到 PyPI (可选)

如果需要发布到 PyPI：

```bash
pip install build twine
python -m build
twine upload dist/*
```

## MkDocs 使用指南

### 安装依赖

```bash
pip install mkdocs-material
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

构建后的文件在 `site/` 目录

### 部署到 GitHub Pages

#### 方式一：使用 GitHub Actions 自动部署

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy docs

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - name: Install dependencies
      run: |
        pip install mkdocs-material
    - name: Build docs
      run: mkdocs build
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./site
```

#### 方式二：手动部署

```bash
mkdocs gh-deploy
```

### 文档结构

```
docs/
├── index.md              # 首页
├── guide/                # 用户指南
│   ├── installation.md
│   ├── quickstart.md
│   └── concepts.md
├── api/                  # API 参考
│   ├── expander.md
│   ├── prompt_mgr.md
│   ├── llm_client.md
│   └── models.md
└── dev/                  # 开发者指南
    ├── testing.md
    └── contributing.md
```

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
```bash
mkdocs build
mkdocs gh-deploy
```

## 注意事项

- 确保 `tests/.env` 不会被提交（已在 `.gitignore` 中）
- GitHub Actions 会在每次推送时自动运行测试
- 文档更新后需要重新构建和部署
