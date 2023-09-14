from fastapi import FastAPI
import uvicorn
from lib.source import (wiki, search_wiki)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}

@app.get("/search/{value}")
async def search(value: str):
    """Search for a wiki"""

    result = search_wiki(value)
    return {"result": result}

@app.get("/wiki/{name}")
async def search(name: str):
    """Get a wiki page"""

    result = wiki(name)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)