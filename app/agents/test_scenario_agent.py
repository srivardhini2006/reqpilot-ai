from app.schemas.brd_state import BRDState
from app.schemas.test_scenario import TestScenarios
from app.services.llm_service import LLMService


class TestScenarioAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        requirements = state.functional_requirements
        use_cases = state.use_cases

        if not requirements:
            return state

        requirements_text = "\n".join(
            f"""
Functional Requirement ID: {req.functional_requirement_id}
Source Requirement: {req.source_requirement_id}
Title: {req.title}
Description: {req.description}
Actor: {req.actor}
Preconditions: {req.preconditions}
Main Flow: {req.main_flow}
Expected Result: {req.expected_result}
"""
            for req in requirements.requirements
        )

        use_case_text = ""

        if use_cases:
            use_case_text = "\n".join(
                f"""
Use Case ID: {uc.use_case_id}
Functional Requirement: {uc.functional_requirement_id}
Title: {uc.title}
Main Flow: {uc.main_flow}
Alternative Flows: {uc.alternative_flows}
Postconditions: {uc.postconditions}
"""
                for uc in use_cases.use_cases
            )

        prompt = f"""
You are a senior QA engineer and requirements analyst.

Generate comprehensive test scenarios from the functional
requirements and use cases below.

Functional Requirements:
{requirements_text}

Use Cases:
{use_case_text}

For each important behavior, consider:

- Positive scenarios
- Negative scenarios
- Boundary scenarios
- Exception scenarios

Return ONLY valid JSON:

{{
    "scenarios": [
        {{
            "scenario_id": "TS-001",
            "source_functional_requirement_id": "FR-001",
            "source_use_case_id": "UC-001",
            "title": "",
            "description": "",
            "scenario_type": "Positive"
        }}
    ]
}}

Rules:
- Maintain traceability.
- Do not invent unsupported functionality.
- Cover both successful and failure conditions where justified.
- Keep scenarios concise.
"""

        result = self.llm.generate_json(prompt)

        state.test_scenarios = TestScenarios(**result)

        return state