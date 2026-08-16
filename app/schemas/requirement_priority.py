from pydantic import BaseModel


class RequirementPriority(BaseModel):
    requirement_id: str
    priority: str
    reason: str


class RequirementPriorities(BaseModel):
    priorities: list[RequirementPriority]