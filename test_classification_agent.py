from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)

from app.agents.classification_agent import ClassificationAgent


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
                        "The system shall respond to booking "
                        "requests within 2 seconds."
                    ),
                    requirement_type="Non-functional",
                    priority="High"
                ),

                BusinessRequirement(
                    requirement_id="BR-003",
                    description=(
                        "Only authenticated users shall be able "
                        "to access patient records."
                    ),
                    requirement_type="Non-functional",
                    priority="High"
                ),

                BusinessRequirement(
                    requirement_id="BR-004",
                    description=(
                        "The system shall be available 99.9% "
                        "of the time."
                    ),
                    requirement_type="Non-functional",
                    priority="High"
                )
            ]
        )
    )

    agent = ClassificationAgent()

    updated_state = agent.analyze(state)

    print("\n===== REQUIREMENT CLASSIFICATION =====")
    print(updated_state.requirement_classifications)


if __name__ == "__main__":
    main()