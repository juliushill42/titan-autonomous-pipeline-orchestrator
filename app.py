from fastapi import FastAPI
from agent import Agent25
app = FastAPI(title="Autonomous-Pipeline-Orchestrator")
agent = Agent25()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
