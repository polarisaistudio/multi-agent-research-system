# tests/test_researcher.py
from src.agents.researcher import researcher_node
from src.state import ResearchState

def test_researcher_finds_papers():
    """Test that researcher can find papers."""
    state = ResearchState(
        query="transformer architecture",
        papers=[], insights=[], report="",
        errors=[], iteration=0
    )

    result = researcher_node(state)

    assert "papers" in result
    assert len(result["papers"]) > 0
    assert result["papers"][0]["source"] == "arxiv"
    print(f"Found {len(result['papers'])} papers")

def test_researcher_handles_bad_query():
    """Test error handling with nonsense query."""
    state = ResearchState(
        query="xyzabc123invalid",
        papers=[], insights=[], report="",
        errors=[], iteration=0
    )

    result = researcher_node(state)
    assert "papers" in result or "errors" in result
    print("Handles bad queries gracefully")
