from knowai_sse.models import PlanetContext, SearchChannel, SearchInstruction, SSEOutput


def test_planet_context_creation():
    context = PlanetContext(
        theme="AI",
        values_map={"radical": 0.8, "ethics": 0.2}
    )
    assert context.theme == "AI"
    assert context.values_map == {"radical": 0.8, "ethics": 0.2}


def test_search_instruction_creation():
    instruction = SearchInstruction(
        channel=SearchChannel.ARXIV,
        query="artificial intelligence",
        time_range="latest"
    )
    assert instruction.channel == SearchChannel.ARXIV
    assert instruction.query == "artificial intelligence"


def test_sse_output_creation():
    instructions = [
        SearchInstruction(
            channel=SearchChannel.WEB,
            query="AI ethics",
            time_range="past_week"
        ),
        SearchInstruction(
            channel=SearchChannel.ARXIV,
            query="machine learning",
            time_range="latest"
        ),
    ]
    output = SSEOutput(instructions=instructions)
    assert len(output.instructions) == 2
