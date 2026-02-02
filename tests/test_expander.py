from unittest.mock import AsyncMock, patch

import pytest

from knowai_sse.core.expander import Expander
from knowai_sse.exceptions import LLMParseError
from knowai_sse.models import PlanetContext, SearchChannel


class TestExpander:

    @pytest.fixture
    def expander(self):
        return Expander(
            api_key="test-key",
            base_url="https://api.test.com",
            model="test-model"
        )

    @pytest.fixture
    def context(self):
        return PlanetContext(
            theme="具身智能",
            values_map={"radical": 0.8, "ethics": 0.2}
        )

    def test_init(self, expander):
        assert expander.prompt_mgr is not None
        assert expander.llm_client is not None
        assert expander.llm_client.api_key == "test-key"

    @pytest.mark.asyncio
    async def test_expand_success(self, expander, context):
        mock_response = '''{
  "instructions": [
    {
      "channel": "arxiv",
      "query": "embodied intelligence robotics",
      "time_range": "latest"
    },
    {
      "channel": "web",
      "query": "embodied AI ethics filetype:pdf",
      "time_range": "past_week"
    }
  ]
}'''

        with patch.object(
            expander.llm_client,
            'chat_completion',
            new=AsyncMock(return_value=mock_response)
        ):
            result = await expander.expand(context)
            assert len(result.instructions) == 2
            assert result.instructions[0].channel == SearchChannel.ARXIV
            assert result.instructions[1].channel == SearchChannel.WEB

    @pytest.mark.asyncio
    async def test_expand_with_invalid_json(self, expander, context):
        mock_response = "Invalid JSON response"

        with patch.object(
            expander.llm_client,
            'chat_completion',
            new=AsyncMock(return_value=mock_response)
        ):
            with pytest.raises(LLMParseError, match="JSON 解析失败"):
                await expander.expand(context)

    @pytest.mark.asyncio
    async def test_close(self, expander):
        with patch.object(expander.llm_client, 'close', new=AsyncMock()) as mock_close:
            await expander.close()
            mock_close.assert_called_once()
