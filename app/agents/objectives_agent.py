from app.schemas.brd_state import BRDState
from app.schemas.project_objectives import ProjectObjectives
from app.services.llm_service import LLMService


class ObjectivesAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        objectives_text = state.project_objectives.strip()

        if not objectives_text:
            return state

        prompt = f"""
You are a senior Business Analyst specializing in requirements engineering.

Analyze the following Project Objectives section from a BRD.

Project Objectives:
{objectives_text}

Extract all clearly stated business objectives.

Return ONLY valid JSON using exactly this structure:

{{
    "objectives": []
}}

Rules:
- Extract only explicitly stated objectives.
- Do not invent or assume objectives.
- Keep each objective concise.
- Preserve the original meaning.
"""

        result = self.llm.generate_json(prompt)

        state.project_objectives_analysis = ProjectObjectives(**result)

        return state