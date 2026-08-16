from pydantic import BaseModel


class RequirementClassification(BaseModel):
    requirement_id: str
    category: str
    reason: str


class RequirementClassifications(BaseModel):
    classifications: list[RequirementClassification]