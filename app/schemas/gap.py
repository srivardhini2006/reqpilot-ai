from pydantic import BaseModel


class Gap(BaseModel):
    requirement_id: str
    missing_information: str
    reason: str
    clarification_question: str


class Gaps(BaseModel):
    gaps: list[Gap]