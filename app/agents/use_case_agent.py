from app.schemas.brd_state import BRDState
from app.schemas.use_case import UseCases
from app.services.llm_service import LLMService


class UseCaseAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        requirements = state.functional_requirements

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

        prompt = f"""
You are a senior Business Analyst and Functional Specification expert.

Generate structured use cases from the following functional
requirements.

Functional Requirements:

{requirements_text}

Return ONLY valid JSON:

{{
    "use_cases": [
        {{
            "use_case_id": "UC-001",
            "functional_requirement_id": "FR-001",
            "title": "",
            "actor": "",
            "preconditions": [],
            "main_flow": [],
            "alternative_flows": [],
            "postconditions": []
        }}
    ]
}}

Rules:
- Generate one primary use case for each functional requirement.
- Maintain traceability to the FR ID.
- Do not invent unsupported functionality.
- Include realistic alternative flows only when justified.
"""

        result = self.llm.generate_json(prompt)

        state.use_cases = UseCases(**result)

        return state