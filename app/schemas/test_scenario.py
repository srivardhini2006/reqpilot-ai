from pydantic import BaseModel


class TestScenario(BaseModel):
    scenario_id: str
    source_functional_requirement_id: str
    source_use_case_id: str | None = None
    title: str
    description: str
    scenario_type: str


class TestScenarios(BaseModel):
    scenarios: list[TestScenario]