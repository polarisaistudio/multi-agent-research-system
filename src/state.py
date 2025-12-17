# src/state.py
from typing import TypedDict, Annotated, List, Optional
import operator

class Paper(TypedDict):
    title: str
    summary: str
    url: str
    source: str

class ResearchState(TypedDict):
    # Input
    query: str

    # Accumulated by agents
    papers: Annotated[List[Paper], operator.add]
    insights: Annotated[List[str], operator.add]

    # Final output
    report: str

    # Metadata
    errors: Annotated[List[str], operator.add]
    iteration: int
