import os

def read_file(path: str) -> str:
    """Reads text content from a local file."""
    if not os.path.exists(path):
        return f"File not found: {path}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def search_duckduckgo(query: str) -> str:
    """Mock search tool: returns a fake summary"""
    return f"Summary for '{query}' from DuckDuckGo (mock)"
