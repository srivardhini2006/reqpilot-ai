from pydantic import BaseModel


class ClarificationQuestion(BaseModel):
    question_id: str
    source_type: str
    source_reference: str
    question: str
    reason: str


class ClarificationQuestions(BaseModel):
    questions: list[ClarificationQuestion]