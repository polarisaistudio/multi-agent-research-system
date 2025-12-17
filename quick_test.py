# quick_test.py
from dotenv import load_dotenv
load_dotenv()

print("[1/4] Testing OpenAI...")
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
print(f"OK: {llm.invoke('Say OK').content}")

print("[2/4] Testing LangGraph...")
from langgraph.graph import StateGraph, END
from typing import TypedDict
class S(TypedDict):
    m: str
g = StateGraph(S)
g.add_node("n", lambda s: {"m": "OK"})
g.set_entry_point("n")
g.add_edge("n", END)
print(f"OK: {g.compile().invoke({'m': ''})['m']}")

print("[3/4] Testing arXiv...")
import arxiv
p = next(arxiv.Search(query="LLM", max_results=1).results())
print(f"OK: Found '{p.title[:40]}...'")

print("[4/4] Testing Wikipedia...")
import wikipedia
print(f"OK: {wikipedia.summary('LLM', sentences=1)[:50]}...")

print("\nAll systems ready!")
