# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.graph import app as research_app

app = FastAPI(title="Research Assistant API")

class ResearchRequest(BaseModel):
    query: str
    max_papers: int = 5

class ResearchResponse(BaseModel):
    query: str
    papers: list
    report: str
    metrics: dict

@app.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest):
    try:
        initial_state = {
            "query": request.query,
            "papers": [],
            "insights": [],
            "report": "",
            "errors": [],
            "iteration": 0
        }

        result = research_app.invoke(initial_state)

        return ResearchResponse(
            query=request.query,
            papers=result["papers"][:request.max_papers],
            report=result["report"],
            metrics={"papers_found": len(result["papers"])}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}
