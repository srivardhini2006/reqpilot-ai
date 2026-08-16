from pydantic import BaseModel


class BusinessRequirement(BaseModel):
    requirement_id: str
    description: str
    requirement_type: str
    priority: str


class BusinessRequirements(BaseModel):
    requirements: list[BusinessRequirement]