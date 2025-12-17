# src/tools/wiki_tool.py
import wikipedia
from langchain.tools import tool

@tool
def search_wikipedia(query: str) -> str:
    """Get Wikipedia summary for background context."""
    try:
        return wikipedia.summary(query, sentences=5)
    except wikipedia.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=5)
    except Exception as e:
        return f"Error: {str(e)}"

