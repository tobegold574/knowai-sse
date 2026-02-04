# KnowAI SSE

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)

语义种子扩展引擎 (Semantic Seed Expander) - 知智感知层的意图发散器。利用 LLM 的语义理解能力，根据预设的价值观对核心主题进行采样与漂移，生成一组具有高知识密度的搜索指令。

## 功能特性

- **价值观驱动的意图发散**：根据星球价值观生成个性化的搜索指令
- **多渠道支持**：支持 arXiv、Web、RSS 等多种搜索渠道
- **异步设计**：完全异步实现，支持高并发场景
- **类型安全**：基于 Pydantic 的严格类型校验
- **可扩展性**：插件化设计，易于添加新的价值观和搜索渠道

## 安装

```bash
pip install knowai-sse
```

或从源码安装：

```bash
git clone https://github.com/your-org/knowai-sse.git
cd knowai-sse
pip install -e .
```

## 快速开始

```python
import asyncio
from knowai_sse import Expander
from knowai_sse.models import PlanetContext

async def main():
    expander = Expander(
        api_key="your-deepseek-api-key",
        base_url="https://api.deepseek.com"
    )

    context = PlanetContext(
        theme="具身智能",
        values_map={"radical": 0.8, "ethics": 0.2}
    )

    result = await expander.expand(context)
    for instruction in result.instructions:
        print(f"[{instruction.channel}] {instruction.query}")

    await expander.close()

asyncio.run(main())
```

## 核心概念

### 价值观

系统支持以下价值观维度：

- **radical**：侧重前沿实验室、GitHub 趋势、未发表论文
- **ethics**：关注 AI 伦理、数字鸿沟、技术公平性
- **practical**：关注工程实践、应用案例、落地效果
- **academic**：侧重理论基础、学术严谨性、同行评审
- **open_source**：关注开源项目、社区生态、开发者工具

### 搜索渠道

- **arxiv**：学术文献搜索，支持 LaTeX 语法
- **web**：网页搜索，支持 Google Search Operators
- **rss**：RSS 订阅源搜索

## 项目结构

```
knowai-sse/
├── src/
│   └── knowai_sse/
│       ├── core/
│       │   ├── expander.py      # 核心逻辑控制器
│       │   └── prompt_mgr.py    # 提示词管理器
│       ├── models/
│       │   └── schema.py        # 数据契约
│       ├── adapters/
│       │   └── llm_client.py    # LLM 适配器
│       └── exceptions.py        # 异常定义
├── tests/
├── examples/
└── docs/
```

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest tests/ -v

# 运行集成测试（需要设置 DEEPSEEK_API_KEY）
cp tests/.env.example tests/.env
pytest tests/ -v -m "integration"

# 代码格式化
black src/ tests/
ruff check src/ tests/

# 类型检查
mypy src/
```

## 文档

详细文档请访问：[https://tobegold574.github.io/knowai-sse/](https://tobegold574.github.io/knowai-sse/)

## 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件。
