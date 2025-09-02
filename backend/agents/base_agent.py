class BaseAgent:
    def respond(self, query: str) -> str:
        return f"[Agent] Received query: {query}"
