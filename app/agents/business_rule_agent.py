from app.schemas.brd_state import BRDState
from app.schemas.business_rule import BusinessRules
from app.services.llm_service import LLMService


class BusinessRuleAgent:

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

Identify business rules and validation logic from the following
functional requirements.

Functional Requirements:

{requirements_text}

Return ONLY valid JSON:

{{
    "rules": [
        {{
            "rule_id": "BRULE-001",
            "source_requirement_id": "BR-001",
            "rule_description": "",
            "condition": "",
            "expected_behavior": ""
        }}
    ]
}}

Rules:
- Identify only meaningful business rules.
- Do not invent unsupported rules.
- Maintain traceability to the source requirement.
- Return an empty list if no explicit business rules exist.
"""

        result = self.llm.generate_json(prompt)

        state.business_rules = BusinessRules(**result)

        return state