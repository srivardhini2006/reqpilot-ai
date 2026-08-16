from app.schemas.brd_state import BRDState
from app.schemas.requirement_validation import RequirementValidations
from app.services.llm_service import LLMService


class ValidationAgent:

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

Evaluate the following business requirements for readiness for
software development and testing.

Requirements:

{requirements_text}

For every requirement evaluate:

1. Clarity
2. Completeness
3. Testability
4. Specificity
5. Overall status
6. Reason

Use only:
- Pass
- Needs Review

Overall status must be:
- Ready
- Needs Review

Return ONLY valid JSON:

{{
    "validations": [
        {{
            "requirement_id": "BR-001",
            "clarity": "Pass",
            "completeness": "Pass",
            "testability": "Pass",
            "specificity": "Pass",
            "overall_status": "Ready",
            "reason": ""
        }}
    ]
}}

Rules:
- Do not invent information.
- Be conservative.
- A requirement with one or more quality issues should be marked
  "Needs Review".
"""

        result = self.llm.generate_json(prompt)

        state.validation_report = RequirementValidations(**result)

        return state