from app.schemas.brd_state import BRDState
from app.schemas.ambiguity import Ambiguities, Ambiguity
from app.schemas.gap import Gaps, Gap
from app.schemas.conflict import Conflicts, Conflict

from app.agents.clarification_agent import ClarificationAgent


def main():

    state = BRDState(

        ambiguities=Ambiguities(
            ambiguities=[
                Ambiguity(
                    requirement_id="BR-001",
                    text="respond quickly",
                    reason="The response time is not measurable.",
                    clarification_question=""
                )
            ]
        ),

        gaps=Gaps(
            gaps=[
                Gap(
                    requirement_id="BR-002",
                    missing_information="Supported payment methods",
                    reason="Payment methods are not specified.",
                    clarification_question=""
                )
            ]
        ),

        conflicts=Conflicts(
            conflicts=[
                Conflict(
                    requirement_id_1="BR-003",
                    requirement_id_2="BR-004",
                    conflict_description=(
                        "The requirements specify contradictory "
                        "appointment cancellation rules."
                    ),
                    reason="One allows cancellation anytime while "
                          "the other restricts cancellation within 24 hours.",
                    clarification_question=""
                )
            ]
        )
    )

    agent = ClarificationAgent()

    updated_state = agent.analyze(state)

    print("\n===== CLARIFICATION QUESTIONS =====")
    print(updated_state.clarification_questions)


if __name__ == "__main__":
    main()