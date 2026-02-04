# PromptManager

Prompt manager responsible for building dynamic prompts based on values.

## Class

### PromptManager

```python
class PromptManager:
    def __init__(self)
```

## Methods

### build_prompts

```python
def build_prompts(self, theme: str, values_map: Dict[str, float]) -> tuple[str, str]
```

Build system prompt and user prompt.

**Parameters:**

- `theme` (str): Core theme
- `values_map` (Dict[str, float]): Value weight mapping

**Returns:**

- `tuple[str, str]`: (system prompt, user prompt)

**Example:**

```python
mgr = PromptManager()
system_prompt, user_prompt = mgr.build_prompts(
    theme="Machine Learning",
    values_map={"academic": 0.9}
)
```

### build_system_prompt

```python
def build_system_prompt(self, values_map: Dict[str, float]) -> str
```

Build system prompt based on values.

### build_user_prompt

```python
def build_user_prompt(self, theme: str) -> str
```

Build user prompt based on theme.

## Supported Values

- `radical`: Radicalism
- `ethics`: Ethical Concern
- `practical`: Pragmatism
- `academic`: Academic Rigor
- `open_source`: Open Source Spirit
