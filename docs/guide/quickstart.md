# 快速开始

## 基本使用

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

## 使用不同的价值观

```python
context = PlanetContext(
    theme="机器学习",
    values_map={
        "academic": 0.7,
        "practical": 0.3
    }
)
```

## 处理结果

```python
result = await expander.expand(context)

for instruction in result.instructions:
    print(f"渠道: {instruction.channel}")
    print(f"查询: {instruction.query}")
    print(f"时间范围: {instruction.time_range}")
    print("---")
```

## 错误处理

```python
from knowai_sse.exceptions import LLMParseError, LLMTimeoutError

try:
    result = await expander.expand(context)
except LLMParseError as e:
    print(f"解析失败: {e}")
except LLMTimeoutError as e:
    print(f"请求超时: {e}")
```
