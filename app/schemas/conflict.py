from pydantic import BaseModel


class Conflict(BaseModel):
    requirement_id_1: str
    requirement_id_2: str
    conflict_description: str
    reason: str
    clarification_question: str


class Conflicts(BaseModel):
    conflicts: list[Conflict]