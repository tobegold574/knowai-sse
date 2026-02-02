# 测试指南

## 运行测试

### 运行所有测试

```bash
pytest tests/ -v
```

### 运行单元测试

```bash
pytest tests/ -v -m "not integration"
```

### 运行集成测试

集成测试需要真实的 API 密钥：

```bash
cp tests/.env.example tests/.env
# 编辑 tests/.env，填入真实的 DEEPSEEK_API_KEY
pytest tests/ -v -m "integration"
```

## 测试结构

```
tests/
├── test_schema.py       # 数据模型测试
├── test_prompt_mgr.py   # 提示词管理器测试
├── test_llm_client.py   # LLM 客户端测试
├── test_expander.py     # 核心扩展器测试
└── test_integration.py  # 集成测试
```

## 编写测试

### 单元测试

单元测试使用 mock 对象，不需要真实的 API 调用。

```python
import pytest
from unittest.mock import AsyncMock, patch
from knowai_sse import Expander

@pytest.mark.asyncio
async def test_expand_success():
    expander = Expander(api_key="test-key")
    context = PlanetContext(theme="测试", values_map={})
    
    mock_response = '{"instructions": []}'
    with patch.object(expander.llm_client, 'chat_completion', new=AsyncMock(return_value=mock_response)):
        result = await expander.expand(context)
        assert len(result.instructions) == 0
```

### 集成测试

集成测试使用真实的 API 调用。

```python
import os
from dotenv import load_dotenv
import pytest
from knowai_sse import Expander

load_dotenv()

@pytest.mark.integration
@pytest.mark.asyncio
async def test_real_api_call():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        pytest.skip("DEEPSEEK_API_KEY not set")
    
    expander = Expander(api_key=api_key)
    # 测试真实 API 调用
```

## 测试标记

- `@pytest.mark.asyncio`: 标记异步测试
- `@pytest.mark.integration`: 标记集成测试
