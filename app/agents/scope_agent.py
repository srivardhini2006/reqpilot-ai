from app.schemas.brd_state import BRDState
from app.schemas.project_scope import ProjectScope
from app.services.llm_service import LLMService


class ScopeAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        scope_text = state.project_scope.strip()

        if not scope_text:
            return state

        prompt = f"""
You are a senior Business Analyst specializing in requirements engineering.

Analyze the following Project Scope section from a BRD.

Project Scope:
{scope_text}

Extract:

1. In-scope items
2. Out-of-scope items

Return ONLY valid JSON using exactly this structure:

{{
    "in_scope": [],
    "out_of_scope": []
}}

Rules:
- Extract only explicitly stated information.
- Do not invent or assume scope items.
- Preserve the original meaning.
- Keep each item concise.
"""

        result = self.llm.generate_json(prompt)

        state.project_scope_analysis = ProjectScope(**result)

        return state