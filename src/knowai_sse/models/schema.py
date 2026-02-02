from enum import Enum
from typing import Dict, List

from pydantic import BaseModel, Field


class SearchChannel(str, Enum):
    ARXIV = "arxiv"
    WEB = "web"
    RSS = "rss"


class PlanetContext(BaseModel):
    theme: str = Field(..., description="核心主题")
    values_map: Dict[str, float] = Field(
        default_factory=dict,
        description="价值观权重映射，如 {'radical': 0.8, 'ethics': 0.2}"
    )


class SearchInstruction(BaseModel):
    channel: SearchChannel = Field(..., description="搜索渠道")
    query: str = Field(..., description="搜索查询语句")
    time_range: str = Field(default="latest", description="时间范围")


class SSEOutput(BaseModel):
    instructions: List[SearchInstruction] = Field(
        default_factory=list,
        description="搜索指令集"
    )
