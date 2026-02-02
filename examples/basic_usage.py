import asyncio
from knowai_sse import Expander
from knowai_sse.models import PlanetContext


async def main():
    expander = Expander(
        api_key="your-deepseek-api-key",
        base_url="https://api.deepseek.com",
        model="deepseek-chat"
    )

    context = PlanetContext(
        theme="具身智能",
        values_map={
            "radical": 0.8,
            "ethics": 0.2
        }
    )

    try:
        result = await expander.expand(context)
        print(f"Generated {len(result.instructions)} search instructions:")
        for idx, instruction in enumerate(result.instructions, 1):
            print(f"{idx}. [{instruction.channel}] {instruction.query} ({instruction.time_range})")
    finally:
        await expander.close()


if __name__ == "__main__":
    asyncio.run(main())
