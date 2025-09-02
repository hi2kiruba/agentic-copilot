import sys
import os

# Add the parent folder (backend) to sys.path so Python can find 'agents'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Absolute imports from the 'agents' package
from agents.tools import read_file, search_duckduckgo
from agents.prompt_helper import validate_output

def answer_with_sources(query: str, file_path: str = None):
    search_result = search_duckduckgo(query)
    file_content = read_file(file_path) if file_path else ""
    combined_answer = f"{search_result}\n{file_content}" if file_content else search_result

    raw_output = {
        "answer": combined_answer,
        "sources": ["DuckDuckGo (mock)"] + ([file_path] if file_path else [])
    }
    return validate_output(raw_output)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Week 1 Lab: Answer with sources CLI")
    parser.add_argument("query", type=str, help="Your query")
    parser.add_argument("--file", type=str, help="Optional local file path", default=None)
    args = parser.parse_args()

    result = answer_with_sources(args.query, args.file)
    # Option 2: Use Pydantic v2 JSON method
print(result.model_dump_json(indent=2))
