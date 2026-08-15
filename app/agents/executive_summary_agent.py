from app.schemas.brd_state import BRDState
from app.schemas.business_context import BusinessContext
from app.services.llm_service import LLMService


class ExecutiveSummaryAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        executive_summary = state.executive_summary.strip()

        if not executive_summary:
            return state

        prompt = f"""
You are a senior Business Analyst specializing in requirements engineering.

Analyze the following Executive Summary from a Business Requirements Document.

Executive Summary:
{executive_summary}

Extract:

1. Business domain
2. Business problem
3. Proposed solution
4. Business goal
5. Expected benefits

Return ONLY valid JSON in exactly this structure:

{{
    "domain": "",
    "business_problem": "",
    "proposed_solution": "",
    "business_goal": "",
    "expected_benefits": []
}}

Rules:
- Do not invent information.
- If information is not specified, use "Not specified".
- Keep the information concise.
"""

        result = self.llm.generate_json(prompt)

        state.business_context = BusinessContext(**result)

        return state