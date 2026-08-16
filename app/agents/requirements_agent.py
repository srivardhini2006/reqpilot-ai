from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import BusinessRequirements
from app.services.llm_service import LLMService


class RequirementsAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        requirements_text = state.business_requirements.strip()

        if not requirements_text:
            return state

        prompt = f"""
You are a senior Business Analyst specializing in requirements engineering.

Analyze the following Business Requirements section from a BRD.

Business Requirements:
{requirements_text}

For every clearly stated requirement, extract:

1. Requirement ID
2. Requirement description
3. Requirement type
4. Priority

Return ONLY valid JSON using exactly this structure:

{{
    "requirements": [
        {{
            "requirement_id": "BR-001",
            "description": "",
            "requirement_type": "",
            "priority": ""
        }}
    ]
}}

Rules:
- Extract only explicitly stated requirements.
- Do not invent requirements.
- Preserve the original meaning.
- If an ID is not provided, create a sequential ID.
- If type is unclear, use "Not specified".
- If priority is unclear, use "Not specified".
"""

        result = self.llm.generate_json(prompt)

        state.business_requirements_analysis = BusinessRequirements(**result)

        return state