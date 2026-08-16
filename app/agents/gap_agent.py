from app.schemas.brd_state import BRDState
from app.schemas.gap import Gaps
from app.services.llm_service import LLMService


class GapAgent:

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

Analyze the following business requirements and identify important
missing information that developers or testers would need.

Requirements:

{requirements_text}

For every meaningful gap, identify:

1. Requirement ID
2. Missing information
3. Why it is important
4. Clarification question

Return ONLY valid JSON:

{{
    "gaps": [
        {{
            "requirement_id": "BR-001",
            "missing_information": "",
            "reason": "",
            "clarification_question": ""
        }}
    ]
}}

Rules:
- Do not invent requirements.
- Do not flag unnecessary information.
- Focus on information that affects implementation or testing.
"""

        result = self.llm.generate_json(prompt)

        state.gaps = Gaps(**result)

        return state