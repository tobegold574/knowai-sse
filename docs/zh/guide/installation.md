# 安装指南

## 环境要求

- Python 3.11 或更高版本

## 使用 pip 安装

```bash
pip install knowai-sse
```

## 从源码安装

```bash
git clone https://github.com/your-org/knowai-sse.git
cd knowai-sse
pip install -e .
```

## 开发环境安装

```bash
pip install -e ".[dev]"
```

这将安装以下开发工具：

- pytest：测试框架
- pytest-asyncio：异步测试支持
- black：代码格式化
- ruff：代码检查
- mypy：类型检查

## 验证安装

```bash
python -c "from knowai_sse import Expander; print('安装成功！')"
```
