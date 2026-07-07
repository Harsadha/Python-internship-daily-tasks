from pydantic import BaseModel

class PromptRequest(BaseModel):
    employee_id: int
    prompt: str