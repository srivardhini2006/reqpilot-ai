from pydantic import BaseModel


class RequirementValidation(BaseModel):
    requirement_id: str
    clarity: str
    completeness: str
    testability: str
    specificity: str
    overall_status: str
    reason: str


class RequirementValidations(BaseModel):
    validations: list[RequirementValidation]