# Expander

Core logic controller that coordinates PromptManager and LLMClient to complete intent expansion.

## Class

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

**Parameters:**

- `api_key` (str): LLM API key
- `base_url` (str): API base URL, defaults to DeepSeek
- `model` (str): Model name to use, defaults to `deepseek-chat`
- `timeout` (int): Request timeout in seconds, defaults to 30

## Methods

### expand

```python
async def expand(self, context: PlanetContext) -> SSEOutput
```

Expand search instructions based on given context.

**Parameters:**

- `context` (PlanetContext): Context object containing theme and values

**Returns:**

- `SSEOutput`: Output object containing search instructions

**Example:**

```python
context = PlanetContext(
    theme="Embodied Intelligence",
    values_map={"radical": 0.8, "ethics": 0.2}
)
result = await expander.expand(context)
```

### close

```python
async def close(self)
```

Close LLM client connection.

## Exceptions

- `LLMParseError`: Response parsing failed
- `LLMTimeoutError`: Request timeout
