# KnowAI SSE

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)
[![中文文档](https://img.shields.io/badge/文档-中文-red.svg)](README.zh.md)

Semantic Seed Expander - An intent expander for the KnowAI perception layer. Leveraging LLM's semantic understanding capabilities, it samples and drifts from core themes based on preset values to generate a set of high-knowledge-density search instructions.

## Features

- **Value-driven Intent Expansion**: Generate personalized search instructions based on planetary values
- **Multi-channel Support**: Support for arXiv, Web, RSS, and other search channels
- **Asynchronous Design**: Fully async implementation supporting high-concurrency scenarios
- **Type Safety**: Strict type validation based on Pydantic
- **Extensibility**: Plugin-based design, easy to add new values and search channels

## Installation

```bash
pip install knowai-sse
```

Or install from source:

```bash
git clone https://github.com/tobegold574/knowai-sse.git
cd knowai-sse
pip install -e .
```

## Quick Start

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
        theme="Embodied Intelligence",
        values_map={"radical": 0.8, "ethics": 0.2}
    )

    result = await expander.expand(context)
    for instruction in result.instructions:
        print(f"[{instruction.channel}] {instruction.query}")

    await expander.close()

asyncio.run(main())
```

## Core Concepts

### Values

The system supports the following value dimensions:

- **radical**: Focus on frontier labs, GitHub trends, unpublished papers
- **ethics**: Focus on AI ethics, digital divide, technological fairness
- **practical**: Focus on engineering practices, application cases, implementation effects
- **academic**: Focus on theoretical foundations, academic rigor, peer review
- **open_source**: Focus on open source projects, community ecosystem, developer tools

### Search Channels

- **arxiv**: Academic literature search, supports LaTeX syntax
- **web**: Web search, supports Google Search Operators
- **rss**: RSS subscription source search

## Project Structure

```
knowai-sse/
├── src/
│   └── knowai_sse/
│       ├── core/
│       │   ├── expander.py      # Core logic controller
│       │   └── prompt_mgr.py    # Prompt manager
│       ├── models/
│       │   └── schema.py        # Data contracts
│       ├── adapters/
│       │   └── llm_client.py    # LLM adapter
│       └── exceptions.py        # Exception definitions
├── tests/
├── examples/
└── docs/
```

## Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run integration tests (requires DEEPSEEK_API_KEY)
cp tests/.env.example tests/.env
pytest tests/ -v -m "integration"

# Code formatting
black src/ tests/
ruff check src/ tests/

# Type checking
mypy src/
```

## Documentation

For detailed documentation, visit: [https://tobegold574.github.io/knowai-sse/](https://tobegold574.github.io/knowai-sse/)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT License - See [LICENSE](LICENSE) file for details.
