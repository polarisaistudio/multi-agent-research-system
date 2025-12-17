# tests/test_analyzer.py
def test_analyzer_extracts_insights():
    """Test that analyzer generates insights from papers."""
    state = ResearchState(
        query="LLM efficiency",
        papers=[
            {"title": "Efficient Transformers", "summary": "Survey of techniques...", "url": "...", "source": "arxiv"},
            {"title": "Quantization Methods", "summary": "We explore...", "url": "...", "source": "arxiv"}
        ],
        insights=[], report="", errors=[], iteration=1
    )

    result = analyzer_node(state)

    assert "insights" in result
    assert len(result["insights"]) > 0
    print(f"Generated {len(result['insights'])} insights")
