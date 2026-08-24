from pydantic import BaseModel


class FunctionalRequirement(BaseModel):
    functional_requirement_id: str
    source_requirement_id: str
    title: str
    description: str
    actor: str
    preconditions: list[str]
    main_flow: list[str]
    expected_result: str


class FunctionalRequirements(BaseModel):
    requirements: list[FunctionalRequirement]