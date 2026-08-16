from pydantic import BaseModel


class RequirementTrace(BaseModel):
    business_requirement_id: str
    functional_requirement_id: str | None = None
    use_case_id: str | None = None
    test_case_id: str | None = None


class RequirementTraces(BaseModel):
    traces: list[RequirementTrace]
    