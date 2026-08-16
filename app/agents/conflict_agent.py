from app.schemas.brd_state import BRDState
from app.schemas.conflict import Conflicts
from app.services.llm_service import LLMService


class ConflictAgent:

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

Analyze the following business requirements and identify genuine
logical conflicts between them.

Requirements:

{requirements_text}

For every conflict, identify:

1. Requirement ID 1
2. Requirement ID 2
3. Conflict description
4. Why they conflict
5. Clarification question

Return ONLY valid JSON:

{{
    "conflicts": [
        {{
            "requirement_id_1": "BR-001",
            "requirement_id_2": "BR-002",
            "conflict_description": "",
            "reason": "",
            "clarification_question": ""
        }}
    ]
}}

Rules:
- Compare requirements against each other.
- Only report genuine contradictions.
- Do not report requirements merely because they are related.
- Do not invent information.
"""

        result = self.llm.generate_json(prompt)

        state.conflicts = Conflicts(**result)

        return state