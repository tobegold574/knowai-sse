# 数据模型

定义了 KnowAI SSE 的数据契约。

## PlanetContext

星球上下文，包含核心主题和价值观映射。

```python
class PlanetContext(BaseModel):
    theme: str
    values_map: Dict[str, float]
```

**字段：**

- `theme` (str): 核心主题
- `values_map` (Dict[str, float]): 价值观权重映射

**示例：**

```python
context = PlanetContext(
    theme="具身智能",
    values_map={"radical": 0.8, "ethics": 0.2}
)
```

## SearchInstruction

搜索指令，定义单个搜索任务。

```python
class SearchInstruction(BaseModel):
    channel: SearchChannel
    query: str
    time_range: str
```

**字段：**

- `channel` (SearchChannel): 搜索渠道（arxiv/web/rss）
- `query` (str): 搜索查询语句
- `time_range` (str): 时间范围（latest/past_24h/past_week/past_month）

## SearchChannel

搜索渠道枚举。

```python
class SearchChannel(str, Enum):
    ARXIV = "arxiv"
    WEB = "web"
    RSS = "rss"
```

## SSEOutput

扩展器输出，包含搜索指令集。

```python
class SSEOutput(BaseModel):
    instructions: List[SearchInstruction]
```

**字段：**

- `instructions` (List[SearchInstruction]): 搜索指令列表

**示例：**

```python
result = await expander.expand(context)
for instruction in result.instructions:
    print(f"[{instruction.channel}] {instruction.query}")
```
