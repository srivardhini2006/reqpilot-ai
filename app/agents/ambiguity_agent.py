from app.schemas.brd_state import BRDState
from app.schemas.ambiguity import Ambiguities
from app.services.llm_service import LLMService


class AmbiguityAgent:

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

Analyze the following business requirements and identify meaningful ambiguities.

Requirements:

{requirements_text}

For every ambiguity, identify:

1. Requirement ID
2. Ambiguous text
3. Why it is ambiguous
4. Clarification question

Return ONLY valid JSON:

{{
    "ambiguities": [
        {{
            "requirement_id": "BR-001",
            "text": "",
            "reason": "",
            "clarification_question": ""
        }}
    ]
}}

Rules:
- Do not invent ambiguities.
- Only identify meaningful ambiguity.
- Look for vague, subjective, undefined, or non-measurable language.
"""

        result = self.llm.generate_json(prompt)

        state.ambiguities = Ambiguities(**result)

        return state