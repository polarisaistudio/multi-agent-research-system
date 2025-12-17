# src/agents/writer.py
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from src.state import ResearchState

WRITER_PROMPT = """You are a technical writer.

Query: {query}

Key Insights:
{insights}

Source Papers:
{papers}

Write a 500-word research summary that:
1. Opens with the main finding
2. Explains key insights with citations
3. Notes limitations or gaps
4. Concludes with implications

Use format: [1], [2] for citations."""

def writer_node(state: ResearchState) -> dict:
    """Write final research report."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    insights_text = "\n".join(state["insights"])
    papers_text = "\n".join(
        f"[{i}] {p['title']}" for i, p in enumerate(state["papers"], 1)
    )

    prompt = ChatPromptTemplate.from_template(WRITER_PROMPT)
    messages = prompt.format_messages(
        query=state["query"],
        insights=insights_text,
        papers=papers_text
    )

    response = llm.invoke(messages)

    return {"report": response.content}
