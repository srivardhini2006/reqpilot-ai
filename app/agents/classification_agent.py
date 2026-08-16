from app.schemas.brd_state import BRDState
from app.schemas.requirement_classification import RequirementClassifications
from app.services.llm_service import LLMService


class ClassificationAgent:

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
You are a senior Business Analyst and Requirements Engineer.

Classify each of the following business requirements.

Requirements:

{requirements_text}

Choose exactly one category for each requirement:

- Functional
- Non-Functional
- Security
- Performance
- Usability
- Availability
- Data
- Integration
- Business

Return ONLY valid JSON:

{{
    "classifications": [
        {{
            "requirement_id": "BR-001",
            "category": "Functional",
            "reason": ""
        }}
    ]
}}

Rules:
- Choose the single best category.
- Do not invent information.
- Base the classification only on the requirement.
"""

        result = self.llm.generate_json(prompt)

        state.requirement_classifications = RequirementClassifications(
            **result
        )

        return state