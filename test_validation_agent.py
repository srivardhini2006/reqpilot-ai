from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)

from app.agents.validation_agent import ValidationAgent


def main():

    state = BRDState(
        business_requirements_analysis=BusinessRequirements(
            requirements=[
                BusinessRequirement(
                    requirement_id="BR-001",
                    description=(
                        "The system shall allow registered customers "
                        "to book an available appointment slot."
                    ),
                    requirement_type="Functional",
                    priority="High"
                ),

                BusinessRequirement(
                    requirement_id="BR-002",
                    description=(
                        "The system shall respond quickly and provide "
                        "a user-friendly booking experience."
                    ),
                    requirement_type="Functional",
                    priority="High"
                )
            ]
        )
    )

    agent = ValidationAgent()

    updated_state = agent.analyze(state)

    print("\n===== REQUIREMENT VALIDATION =====")
    print(updated_state.validation_report)


if __name__ == "__main__":
    main()