# PromptManager

提示词管理器，负责根据价值观构建动态提示词。

## 类

### PromptManager

```python
class PromptManager:
    def __init__(self)
```

## 方法

### build_prompts

```python
def build_prompts(self, theme: str, values_map: Dict[str, float]) -> tuple[str, str]
```

构建系统提示词和用户提示词。

**参数：**

- `theme` (str): 核心主题
- `values_map` (Dict[str, float]): 价值观权重映射

**返回：**

- `tuple[str, str]`: (系统提示词, 用户提示词)

**示例：**

```python
mgr = PromptManager()
system_prompt, user_prompt = mgr.build_prompts(
    theme="机器学习",
    values_map={"academic": 0.9}
)
```

### build_system_prompt

```python
def build_system_prompt(self, values_map: Dict[str, float]) -> str
```

根据价值观构建系统提示词。

### build_user_prompt

```python
def build_user_prompt(self, theme: str) -> str
```

根据主题构建用户提示词。

## 支持的价值观

- `radical`: 激进主义
- `ethics`: 伦理关怀
- `practical`: 实用主义
- `academic`: 学术严谨
- `open_source`: 开源精神
