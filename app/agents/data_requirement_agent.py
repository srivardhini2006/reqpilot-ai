from app.schemas.brd_state import BRDState
from app.schemas.data_requirement import DataRequirements
from app.services.llm_service import LLMService


class DataRequirementAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        requirements = state.functional_requirements

        if not requirements:
            return state

        requirements_text = "\n".join(
            f"""
Functional Requirement ID: {req.functional_requirement_id}
Source Requirement: {req.source_requirement_id}
Title: {req.title}
Description: {req.description}
Actor: {req.actor}
Preconditions: {req.preconditions}
Main Flow: {req.main_flow}
Expected Result: {req.expected_result}
"""
            for req in requirements.requirements
        )

        prompt = f"""
You are a senior Business Analyst and Functional Specification expert.

Identify the important data entities required by these functional
requirements.

Functional Requirements:

{requirements_text}

For each entity provide:

- Entity ID
- Source requirement ID
- Entity name
- Description
- Important attributes
- Relationships

Return ONLY valid JSON:

{{
    "entities": [
        {{
            "entity_id": "ENT-001",
            "source_requirement_id": "BR-001",
            "entity_name": "",
            "description": "",
            "attributes": [],
            "relationships": []
        }}
    ]
}}

Rules:
- Identify only entities supported by the requirements.
- Do not invent unnecessary entities.
- Do not provide database-specific implementation.
- Maintain traceability.
"""

        result = self.llm.generate_json(prompt)

        state.data_requirements = DataRequirements(**result)

        return state