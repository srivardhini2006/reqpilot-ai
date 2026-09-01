from pydantic import BaseModel


class TestTrace(BaseModel):
    business_requirement_id: str
    functional_requirement_id: str
    use_case_id: str | None = None
    scenario_id: str
    test_case_id: str


class TestTraceability(BaseModel):
    traces: list[TestTrace]