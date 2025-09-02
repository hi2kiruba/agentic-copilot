from pydantic import BaseModel

class OutputSchema(BaseModel):
    answer: str
    sources: list[str]

def validate_output(output: dict) -> OutputSchema:
    return OutputSchema(**output)
