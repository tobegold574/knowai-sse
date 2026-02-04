# Expander

核心逻辑控制器，协调 PromptManager 和 LLMClient 完成意图扩展。

## 类

### Expander

```python
class Expander:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.deepseek.com",
        model: str = "deepseek-chat",
        timeout: int = 30
    )
```

**参数：**

- `api_key` (str): LLM API 密钥
- `base_url` (str): API 基础 URL，默认为 DeepSeek
- `model` (str): 使用的模型名称，默认为 `deepseek-chat`
- `timeout` (int): 请求超时时间（秒），默认为 30

## 方法

### expand

```python
async def expand(self, context: PlanetContext) -> SSEOutput
```

根据给定的上下文扩展搜索指令。

**参数：**

- `context` (PlanetContext): 包含主题和价值观的上下文对象

**返回：**

- `SSEOutput`: 包含搜索指令集的输出对象

**示例：**

```python
context = PlanetContext(
    theme="具身智能",
    values_map={"radical": 0.8, "ethics": 0.2}
)
result = await expander.expand(context)
```

### close

```python
async def close(self)
```

关闭 LLM 客户端连接。

## 异常

- `LLMParseError`: 响应解析失败
- `LLMTimeoutError`: 请求超时
