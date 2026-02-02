import json
import re

from pydantic import TypeAdapter

from ..adapters.llm_client import LLMClient
from ..exceptions import LLMParseError
from ..models.schema import PlanetContext, SearchInstruction, SSEOutput
from .prompt_mgr import PromptManager


class Expander:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.deepseek.com",
        model: str = "deepseek-chat",
        timeout: int = 30
    ):
        self.prompt_mgr = PromptManager()
        self.llm_client = LLMClient(
            api_key=api_key,
            base_url=base_url,
            model=model,
            timeout=timeout
        )

    async def expand(self, context: PlanetContext) -> SSEOutput:
        system_prompt, user_prompt = self.prompt_mgr.build_prompts(
            theme=context.theme,
            values_map=context.values_map
        )

        raw_response = await self.llm_client.chat_completion(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

        return self._parse_response(raw_response)

    def _parse_response(self, raw_response: str) -> SSEOutput:
        cleaned_response = self._extract_json(raw_response)

        try:
            data = json.loads(cleaned_response)
            instructions_data = data.get("instructions", [])

            adapter = TypeAdapter(list[SearchInstruction])
            instructions = adapter.validate_python(instructions_data)

            return SSEOutput(instructions=instructions)

        except json.JSONDecodeError as e:
            raise LLMParseError(f"JSON 解析失败: {e}")
        except Exception as e:
            raise LLMParseError(f"响应解析失败: {e}")

    def _extract_json(self, text: str) -> str:
        json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
        matches = re.findall(json_pattern, text)

        if matches:
            return str(matches[0])

        return text

    async def close(self) -> None:
        await self.llm_client.close()
