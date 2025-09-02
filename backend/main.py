from fastapi import FastAPI
from agents.base_agent import BaseAgent


app = FastAPI()
agent = BaseAgent()

@app.get("/")
def read_root():
    return {"message": "Agentic Copilot Backend Running 🚀"}


@app.post("/ask")
def ask_agent(query: str):
    return {"response": agent.respond(query)} 