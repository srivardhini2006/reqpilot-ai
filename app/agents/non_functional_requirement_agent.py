from app.schemas.brd_state import BRDState
from app.schemas.non_functional_requirement import (
    NonFunctionalRequirements
)
from app.services.llm_service import LLMService


class NonFunctionalRequirementAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        requirements = state.business_requirements_analysis

        if not requirements:
            return state

        requirements_text = "\n".join(
            f"""
Requirement ID: {req.requirement_id}
Description: {req.description}
Type: {req.requirement_type}
Priority: {req.priority}
"""
            for req in requirements.requirements
        )

        prompt = f"""
You are a senior Business Analyst and Functional Specification expert.

Identify non-functional requirements from the following business
requirements.

Business Requirements:

{requirements_text}

Look for:

- Performance
- Security
- Availability
- Reliability
- Scalability
- Usability
- Accessibility
- Maintainability
- Compliance
- Data privacy

Return ONLY valid JSON:

{{
    "requirements": [
        {{
            "nfr_id": "NFR-001",
            "source_requirement_id": "BR-001",
            "category": "",
            "description": "",
            "measurable_criteria": ""
        }}
    ]
}}

Rules:
- Do not invent unsupported requirements.
- Do not invent numerical targets.
- Maintain traceability to the original requirement.
- Return an empty list if no NFRs can be identified.
"""

        result = self.llm.generate_json(prompt)

        state.non_functional_requirements = (
            NonFunctionalRequirements(**result)
        )

        return state