# LLMClient

LLM 适配器，提供统一的异步调用接口。

## 类

### LLMClient

```python
class LLMClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.deepseek.com",
        model: str = "deepseek-chat",
        timeout: int = 30,
        max_retries: int = 3
    )
```

**参数：**

- `api_key` (str): API 密钥
- `base_url` (str): API 基础 URL
- `model` (str): 模型名称
- `timeout` (int): 超时时间（秒）
- `max_retries` (int): 最大重试次数

## 方法

### chat_completion

```python
async def chat_completion(
    self,
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.7,
    max_tokens: int = 2000
) -> str
```

发送聊天完成请求。

**参数：**

- `system_prompt` (str): 系统提示词
- `user_prompt` (str): 用户提示词
- `temperature` (float): 温度参数，控制随机性
- `max_tokens` (int): 最大生成 token 数

**返回：**

- `str`: LLM 响应内容

**异常：**

- `LLMTimeoutError`: 请求超时
- `LLMParseError`: 响应解析失败

### close

```python
async def close(self)
```

关闭客户端连接。

## 特性

- **自动重试**：失败时自动重试，最多 `max_retries` 次
- **超时控制**：支持自定义超时时间
- **异步支持**：完全异步实现，支持高并发
