from app.schemas.brd_state import BRDState
from app.schemas.clarification_question import ClarificationQuestions
from app.services.llm_service import LLMService


class ClarificationAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, state: BRDState) -> BRDState:

        findings = []

        # Ambiguities
        if state.ambiguities:
            for ambiguity in state.ambiguities.ambiguities:
                findings.append({
                    "source_type": "ambiguity",
                    "source_reference": ambiguity.requirement_id,
                    "finding": ambiguity.reason
                })

        # Gaps
        if state.gaps:
            for gap in state.gaps.gaps:
                findings.append({
                    "source_type": "gap",
                    "source_reference": gap.requirement_id,
                    "finding": gap.missing_information
                })

        # Conflicts
        if state.conflicts:
            for conflict in state.conflicts.conflicts:
                findings.append({
                    "source_type": "conflict",
                    "source_reference": (
                        f"{conflict.requirement_id_1}, "
                        f"{conflict.requirement_id_2}"
                    ),
                    "finding": conflict.conflict_description
                })

        if not findings:
            state.clarification_questions = ClarificationQuestions(
                questions=[]
            )
            return state

        findings_text = "\n".join(
            f"""
Source Type: {item['source_type']}
Reference: {item['source_reference']}
Finding: {item['finding']}
"""
            for item in findings
        )

        prompt = f"""
You are a senior Business Analyst and Requirements Engineer.

Generate clear clarification questions based on these BRD quality findings:

{findings_text}

Return ONLY valid JSON:

{{
    "questions": [
        {{
            "question_id": "Q-001",
            "source_type": "",
            "source_reference": "",
            "question": "",
            "reason": ""
        }}
    ]
}}

Rules:
- Generate one useful question for each meaningful finding.
- Do not repeat questions.
- Do not invent information.
- Questions must be answerable by a business stakeholder.
- Make questions specific and actionable.
"""

        result = self.llm.generate_json(prompt)

        state.clarification_questions = ClarificationQuestions(**result)

        return state