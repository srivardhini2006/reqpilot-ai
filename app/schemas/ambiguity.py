from pydantic import BaseModel


class Ambiguity(BaseModel):
    requirement_id: str
    text: str
    reason: str
    clarification_question: str


class Ambiguities(BaseModel):
    ambiguities: list[Ambiguity]