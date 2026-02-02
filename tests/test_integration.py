import os

import pytest
from dotenv import load_dotenv

from knowai_sse import Expander
from knowai_sse.models import PlanetContext, SearchChannel

load_dotenv()


@pytest.mark.integration
class TestExpanderIntegration:

    @pytest.fixture
    def api_key(self):
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key or api_key == "your-deepseek-api-key-here":
            pytest.skip("DEEPSEEK_API_KEY not set in .env file")
        return api_key

    @pytest.fixture
    def expander(self, api_key):
        return Expander(
            api_key=api_key,
            base_url="https://api.deepseek.com",
            model="deepseek-chat"
        )

    @pytest.mark.asyncio
    async def test_real_api_call(self, expander):
        context = PlanetContext(
            theme="具身智能",
            values_map={"radical": 0.8, "ethics": 0.2}
        )

        result = await expander.expand(context)

        assert len(result.instructions) > 0
        assert all(isinstance(inst.channel, SearchChannel) for inst in result.instructions)
        assert all(inst.query for inst in result.instructions)
        assert all(inst.time_range for inst in result.instructions)

        await expander.close()
