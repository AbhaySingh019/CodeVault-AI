from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import index_codebase
from engine import LocalCodeVaultEngine

app = FastAPI(title="CodeVault-AI Engine", version="1.0")

# Engine instance initialize
engine = LocalCodeVaultEngine()


class QueryRequest(BaseModel):
    query: str


class IndexRequest(BaseModel):
    repo_path: str = "."


@app.get("/")
def read_root():
    return {
        "status": "online",
        "system": "CodeVault-AI (Offline Snapdragon Engine)",
    }


@app.post("/index")
def trigger_indexing(payload: IndexRequest):
    try:
        table = index_codebase(payload.repo_path)
        if table is None:
            raise HTTPException(status_code=400, detail="No code files found")
        return {
            "status": "success",
            "message": "Codebase successfully indexed!",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search")
def search_and_audit(payload: QueryRequest):
    try:
        response = engine.query_codebase(payload.query)
        return {"query": payload.query, "result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)