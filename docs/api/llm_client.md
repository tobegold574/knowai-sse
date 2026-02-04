# LLMClient

LLM adapter providing unified async call interface.

## Class

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

**Parameters:**

- `api_key` (str): API key
- `base_url` (str): API base URL
- `model` (str): Model name
- `timeout` (int): Timeout in seconds
- `max_retries` (int): Maximum retry count

## Methods

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

Send chat completion request.

**Parameters:**

- `system_prompt` (str): System prompt
- `user_prompt` (str): User prompt
- `temperature` (float): Temperature parameter, controls randomness
- `max_tokens` (int): Maximum generation tokens

**Returns:**

- `str`: LLM response content

**Exceptions:**

- `LLMTimeoutError`: Request timeout
- `LLMParseError`: Response parsing failed

### close

```python
async def close(self)
```

Close client connection.

## Features

- **Auto Retry**: Automatically retry on failure, up to `max_retries` times
- **Timeout Control**: Support custom timeout
- **Async Support**: Fully async implementation, supports high concurrency
