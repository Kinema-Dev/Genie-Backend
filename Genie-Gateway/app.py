from fastapi import FastAPI

app = FastAPI()


@app.post("/run")
async def run_search():
    """Triggers a single search"""
    pass


