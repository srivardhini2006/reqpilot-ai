from app.schemas.brd_state import BRDState
from app.schemas.requirement_priority import RequirementPriorities
from app.services.llm_service import LLMService


class PrioritizationAgent:

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

        business_context = ""

        if state.business_context:
            business_context = f"""
Business Context:
{state.business_context}
"""

        objectives = ""

        if state.project_objectives_analysis:
            objectives = f"""
Project Objectives:
{state.project_objectives_analysis}
"""

        prompt = f"""
You are a senior Business Analyst and Requirements Engineer.

Prioritize the following business requirements using MoSCoW.

{business_context}

{objectives}

Requirements:

{requirements_text}

Choose exactly one:

- Must Have
- Should Have
- Could Have
- Won't Have

Return ONLY valid JSON:

{{
    "priorities": [
        {{
            "requirement_id": "BR-001",
            "priority": "Must Have",
            "reason": ""
        }}
    ]
}}

Rules:
- Base the decision on the provided business context and objectives.
- Do not invent priorities.
- Explain the reasoning briefly.
"""

        result = self.llm.generate_json(prompt)

        state.requirement_priorities = RequirementPriorities(**result)

        return state