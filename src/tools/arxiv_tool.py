# src/tools/arxiv_tool.py (enhanced)
import time
from typing import List

import arxiv
from langchain_core.tools import tool

from src.tools.retry import retry_with_backoff

@tool
@retry_with_backoff(max_retries=3, base_delay=1.0)
def search_arxiv(query: str, max_results: int = 5) -> List[dict]:
    """Search arXiv with automatic retry on failure."""
    try:
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        papers = []
        for result in search.results():
            papers.append({
                "title": result.title,
                "summary": result.summary[:500],
                "url": result.pdf_url,
                "source": "arxiv"
            })
            time.sleep(0.5)

        return papers if papers else [{"error": "No papers found", "query": query}]

    except Exception as e:
        raise Exception(f"arXiv search failed: {e}")
