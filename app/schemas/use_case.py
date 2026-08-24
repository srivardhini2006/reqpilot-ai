from pydantic import BaseModel


class UseCase(BaseModel):
    use_case_id: str
    functional_requirement_id: str
    title: str
    actor: str
    preconditions: list[str]
    main_flow: list[str]
    alternative_flows: list[str]
    postconditions: list[str]


class UseCases(BaseModel):
    use_cases: list[UseCase]