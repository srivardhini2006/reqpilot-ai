from app.schemas.brd_state import BRDState
from app.schemas.traceability import RequirementTraces
from app.services.llm_service import LLMService


class TraceabilityAgent:

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

Create a requirement traceability structure for these business
requirements:

{requirements_text}

For every business requirement:

- Preserve its original requirement ID.
- Generate a corresponding functional requirement ID.
- Use sequential functional requirement IDs such as FR-001, FR-002.
- Set use_case_id to null.
- Set test_case_id to null.

Return ONLY valid JSON:

{{
    "traces": [
        {{
            "business_requirement_id": "BR-001",
            "functional_requirement_id": "FR-001",
            "use_case_id": null,
            "test_case_id": null
        }}
    ]
}}

Rules:
- Every business requirement must have exactly one trace.
- Do not lose any requirements.
- Do not invent additional business requirements.
"""

        result = self.llm.generate_json(prompt)

        state.traceability_matrix = RequirementTraces(**result)

        return state