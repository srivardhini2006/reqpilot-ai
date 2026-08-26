from app.schemas.brd_state import BRDState
from app.schemas.test_case import TestCases
from app.services.llm_service import LLMService


class TestCaseAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        scenarios = state.test_scenarios

        if not scenarios:
            return state

        scenarios_text = "\n".join(
            f"""
Scenario ID: {scenario.scenario_id}
Functional Requirement:
{scenario.source_functional_requirement_id}

Use Case:
{scenario.source_use_case_id}

Title:
{scenario.title}

Description:
{scenario.description}

Scenario Type:
{scenario.scenario_type}
"""
            for scenario in scenarios.scenarios
        )

        prompt = f"""
You are a senior QA engineer.

Generate detailed test cases from the following test scenarios.

Test Scenarios:

{scenarios_text}

For every test scenario generate:

- Test case ID
- Source scenario ID
- Source functional requirement ID
- Title
- Test type
- Preconditions
- Test steps
- Expected results

Return ONLY valid JSON:

{{
    "test_cases": [
        {{
            "test_case_id": "TC-001",
            "source_scenario_id": "TS-001",
            "source_functional_requirement_id": "FR-001",
            "title": "",
            "test_type": "",
            "preconditions": [],
            "test_steps": [],
            "expected_results": []
        }}
    ]
}}

Rules:
- Maintain traceability to the scenario and functional requirement.
- Generate one test case for each scenario.
- Test steps must be concrete and executable.
- Expected results must correspond to the test steps.
- Do not invent unsupported system behavior.
- Return only valid JSON.
"""

        result = self.llm.generate_json(prompt)

        state.test_cases = TestCases(**result)

        return state