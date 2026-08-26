from pydantic import BaseModel


class TestCase(BaseModel):
    test_case_id: str
    source_scenario_id: str
    source_functional_requirement_id: str
    title: str
    test_type: str
    preconditions: list[str]
    test_steps: list[str]
    expected_results: list[str]


class TestCases(BaseModel):
    test_cases: list[TestCase]