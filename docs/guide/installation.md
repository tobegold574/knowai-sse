# Installation Guide

## Requirements

- Python 3.11 or higher

## Install with pip

```bash
pip install knowai-sse
```

## Install from source

```bash
git clone https://github.com/tobegold574/knowai-sse.git
cd knowai-sse
pip install -e .
```

## Development environment

```bash
pip install -e ".[dev]"
```

This will install the following development tools:

- pytest: Testing framework
- pytest-asyncio: Async testing support
- black: Code formatting
- ruff: Code linting
- mypy: Type checking

## Verify installation

```bash
python -c "from knowai_sse import Expander; print('Installation successful!')"
```
