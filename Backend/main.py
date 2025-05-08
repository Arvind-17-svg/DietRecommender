from fastapi import FastAPI,HTTPException
from rag_pipeline import get_qa
from pydantic import BaseModel

app = FastAPI()
qa = get_qa()

class QueryRequest(BaseModel):
    query: str
    

@app.post("/query")
def query_rag(request: QueryRequest):
    try:
        result = qa({"query": request.query})
        return {
            "answer": result["result"],
            "sources": [doc.metadata for doc in result["source_documents"]]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




