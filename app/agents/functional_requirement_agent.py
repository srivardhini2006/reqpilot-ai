from app.schemas.brd_state import BRDState
from app.schemas.functional_requirement import FunctionalRequirements
from app.services.llm_service import LLMService


class FunctionalRequirementAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        requirements = state.business_requirements_analysis

        if not requirements:
            return state

        requirements_text = "\n".join(
            f"{req.requirement_id}: {req.description}"
            for req in requirements.requirements
        )

        prompt = f"""
You are a senior Business Analyst and Functional Specification expert.

Transform the following validated business requirements into
structured functional requirements for an FSD.

Business Requirements:

{requirements_text}

For every requirement generate:

- Functional requirement ID
- Source business requirement ID
- Title
- Description
- Actor
- Preconditions
- Main flow
- Expected result

Return ONLY valid JSON:

{{
    "requirements": [
        {{
            "functional_requirement_id": "FR-001",
            "source_requirement_id": "BR-001",
            "title": "",
            "description": "",
            "actor": "",
            "preconditions": [],
            "main_flow": [],
            "expected_result": ""
        }}
    ]
}}

Rules:
- Maintain traceability to the original BR ID.
- Do not invent unsupported functionality.
- Keep the requirement implementation-neutral.
- Generate one functional requirement for each business requirement.
"""

        result = self.llm.generate_json(prompt)

        state.functional_requirements = FunctionalRequirements(**result)

        return state