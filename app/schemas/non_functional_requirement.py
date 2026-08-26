from pydantic import BaseModel


class NonFunctionalRequirement(BaseModel):
    nfr_id: str
    source_requirement_id: str
    category: str
    description: str
    measurable_criteria: str


class NonFunctionalRequirements(BaseModel):
    requirements: list[NonFunctionalRequirement]