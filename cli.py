# cli.py
from src.graph import app

def research(query: str):
    """Run research pipeline."""
    initial_state = {
        "query": query,
        "papers": [],
        "insights": [],
        "report": "",
        "errors": [],
        "iteration": 0
    }

    result = app.invoke(initial_state)

    print(f"Found {len(result['papers'])} papers")
    print(f"Generated {len(result['insights'])} insights")
    print(f"\nReport:\n{result['report']}")

    return result

if __name__ == "__main__":
    research("transformer efficiency techniques")
