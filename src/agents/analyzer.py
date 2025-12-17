# src/agents/analyzer.py
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from src.state import ResearchState

ANALYZER_PROMPT = """You are a research analyst.

Query: {query}

Papers found:
{papers}

Your task:
1. Identify 3-5 key insights across papers
2. Note any contradictions or gaps
3. Rank findings by relevance

Return insights as a numbered list."""

def analyzer_node(state: ResearchState) -> dict:
    """Analyze research findings."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Format papers for context
    papers_text = ""
    for i, paper in enumerate(state["papers"], 1):
        papers_text += f"{i}. {paper['title']}\n{paper['summary']}\n\n"

    prompt = ChatPromptTemplate.from_template(ANALYZER_PROMPT)
    messages = prompt.format_messages(
        query=state["query"],
        papers=papers_text
    )

    response = llm.invoke(messages)

    # Parse insights from response
    insights = [line.strip() for line in response.content.split("\n")
                if line.strip() and line[0].isdigit()]

    return {"insights": insights}
