import asyncio
from unittest.mock import AsyncMock, patch

import pytest

from knowai_sse.adapters.llm_client import LLMClient
from knowai_sse.exceptions import LLMParseError, LLMTimeoutError


class TestLLMClient:

    @pytest.fixture
    def client(self):
        return LLMClient(
            api_key="test-key",
            base_url="https://api.test.com",
            model="test-model",
            timeout=10
        )

    def test_init(self, client):
        assert client.api_key == "test-key"
        assert client.base_url == "https://api.test.com"
        assert client.model == "test-model"
        assert client.timeout == 10
        assert client.max_retries == 3

    @pytest.mark.asyncio
    async def test_chat_completion_success(self, client):
        mock_response = AsyncMock()
        mock_response.choices = [AsyncMock()]
        mock_response.choices[0].message.content = "Test response"

        with patch.object(
            client.client.chat.completions,
            'create',
            new=AsyncMock(return_value=mock_response)
        ):
            result = await client.chat_completion(
                "System prompt",
                "User prompt"
            )
            assert result == "Test response"

    @pytest.mark.asyncio
    async def test_chat_completion_empty_content(self, client):
        mock_response = AsyncMock()
        mock_response.choices = [AsyncMock()]
        mock_response.choices[0].message.content = None

        with patch.object(
            client.client.chat.completions,
            'create',
            new=AsyncMock(return_value=mock_response)
        ):
            with pytest.raises(LLMParseError, match="LLM 返回空内容"):
                await client.chat_completion(
                    "System prompt",
                    "User prompt"
                )

    @pytest.mark.asyncio
    async def test_chat_completion_timeout(self, client):
        with patch.object(
            client.client.chat.completions,
            'create',
            new=AsyncMock(side_effect=asyncio.TimeoutError)
        ):
            with pytest.raises(LLMTimeoutError, match="LLM 请求超时"):
                await client.chat_completion(
                    "System prompt",
                    "User prompt"
                )

    @pytest.mark.asyncio
    async def test_chat_completion_retry(self, client):
        call_count = [0]

        async def side_effect(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] < 2:
                raise Exception("Temporary error")
            mock_response = AsyncMock()
            mock_response.choices = [AsyncMock()]
            mock_response.choices[0].message.content = (
                "Success after retry"
            )
            return mock_response

        with patch.object(
            client.client.chat.completions,
            'create',
            new=AsyncMock(side_effect=side_effect)
        ):
            result = await client.chat_completion(
                "System prompt",
                "User prompt"
            )
            assert result == "Success after retry"
            assert call_count[0] == 2

    @pytest.mark.asyncio
    async def test_chat_completion_max_retries_exceeded(self, client):
        with patch.object(
            client.client.chat.completions,
            'create',
            new=AsyncMock(side_effect=Exception("Persistent error"))
        ):
            with pytest.raises(LLMParseError, match="LLM 请求失败"):
                await client.chat_completion(
                    "System prompt",
                    "User prompt"
                )

    @pytest.mark.asyncio
    async def test_close(self, client):
        with patch.object(
            client.client,
            'close',
            new=AsyncMock()
        ) as mock_close:
            await client.close()
            mock_close.assert_called_once()
