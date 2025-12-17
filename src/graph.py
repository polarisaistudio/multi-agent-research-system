# src/graph.py
from langgraph.graph import StateGraph, END
from src.state import ResearchState
from src.agents.researcher import researcher_node
from src.agents.analyzer import analyzer_node
from src.agents.writer import writer_node

def should_continue_research(state: ResearchState) -> str:
    """Decide if we need more research."""
    if len(state.get("papers", [])) < 3:
        return "research_more"
    if state.get("iteration", 0) >= 3:
        return "analyze"  # Max iterations
    return "analyze"

def build_research_graph():
    """Build the multi-agent research workflow."""

    graph = StateGraph(ResearchState)

    # Add nodes
    graph.add_node("researcher", researcher_node)
    graph.add_node("analyzer", analyzer_node)
    graph.add_node("writer", writer_node)

    # Set entry point
    graph.set_entry_point("researcher")

    # Add conditional edge
    graph.add_conditional_edges(
        "researcher",
        should_continue_research,
        {
            "research_more": "researcher",
            "analyze": "analyzer"
        }
    )

    # Add remaining edges
    graph.add_edge("analyzer", "writer")
    graph.add_edge("writer", END)

    return graph.compile()

# Create the app
app = build_research_graph()
