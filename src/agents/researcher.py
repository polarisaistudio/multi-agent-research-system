# src/agents/researcher.py
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from src.tools.arxiv_tool import search_arxiv
from src.tools.wiki_tool import search_wikipedia
from src.state import ResearchState

RESEARCHER_PROMPT = """You are a research specialist.

Your task: Find relevant academic papers and background information.

Query: {query}

Available tools:
1. search_arxiv - Find academic papers
2. search_wikipedia - Get background context

Instructions:
1. Search arXiv for 3-5 relevant papers
2. Get Wikipedia context for key terms
3. Return structured findings

Be thorough but focused on the query."""

def create_researcher_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [search_arxiv, search_wikipedia]
    return llm.bind_tools(tools)

def researcher_node(state: ResearchState) -> dict:
    """Execute research agent."""
    agent = create_researcher_agent()

    prompt = ChatPromptTemplate.from_template(RESEARCHER_PROMPT)
    messages = prompt.format_messages(query=state["query"])

    response = agent.invoke(messages)

    # Extract tool calls and execute
    papers = []
    for tool_call in response.tool_calls:
        if tool_call["name"] == "search_arxiv":
            results = search_arxiv.invoke(tool_call["args"])
            papers.extend(results)

    return {"papers": papers, "iteration": state.get("iteration", 0) + 1}
