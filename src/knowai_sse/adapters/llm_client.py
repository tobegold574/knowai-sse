import asyncio

from openai import AsyncOpenAI

from ..exceptions import LLMParseError, LLMTimeoutError


class LLMClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.deepseek.com",
        model: str = "deepseek-chat",
        timeout: int = 30,
        max_retries: int = 3
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.timeout = timeout
        self.max_retries = max_retries
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout
        )

    async def chat_completion(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 2000
    ) -> str:
        retry_count = 0

        while retry_count < self.max_retries:
            try:
                response = await self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=temperature,
                    max_tokens=max_tokens
                )

                content = response.choices[0].message.content

                if not content:
                    raise LLMParseError("LLM 返回空内容")

                return content

            except asyncio.TimeoutError:
                retry_count += 1
                if retry_count >= self.max_retries:
                    raise LLMTimeoutError(f"LLM 请求超时（重试 {retry_count} 次后失败）")
                await asyncio.sleep(1 * retry_count)

            except Exception as e:
                retry_count += 1
                if retry_count >= self.max_retries:
                    raise LLMParseError(f"LLM 请求失败: {e}")
                await asyncio.sleep(1 * retry_count)

        raise LLMParseError("LLM 请求失败：超过最大重试次数")

    async def close(self) -> None:
        await self.client.close()
