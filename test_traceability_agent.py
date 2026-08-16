from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)

from app.agents.traceability_agent import TraceabilityAgent


def main():

    state = BRDState(
        business_requirements_analysis=BusinessRequirements(
            requirements=[
                BusinessRequirement(
                    requirement_id="BR-001",
                    description=(
                        "The system shall allow customers "
                        "to book appointments online."
                    ),
                    requirement_type="Functional",
                    priority="High"
                ),

                BusinessRequirement(
                    requirement_id="BR-002",
                    description=(
                        "The system shall allow customers "
                        "to cancel appointments."
                    ),
                    requirement_type="Functional",
                    priority="High"
                ),

                BusinessRequirement(
                    requirement_id="BR-003",
                    description=(
                        "The system shall send appointment "
                        "confirmation notifications."
                    ),
                    requirement_type="Functional",
                    priority="Medium"
                )
            ]
        )
    )

    agent = TraceabilityAgent()

    updated_state = agent.analyze(state)

    print("\n===== REQUIREMENT TRACEABILITY =====")
    print(updated_state.traceability_matrix)


if __name__ == "__main__":
    main()