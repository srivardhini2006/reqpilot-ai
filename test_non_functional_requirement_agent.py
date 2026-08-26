from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)

from app.agents.non_functional_requirement_agent import (
    NonFunctionalRequirementAgent
)


def main():

    state = BRDState(
        business_requirements_analysis=BusinessRequirements(
            requirements=[

                BusinessRequirement(
                    requirement_id="BR-001",
                    description=(
                        "The system shall allow customers to book "
                        "appointments online."
                    ),
                    requirement_type="Functional",
                    priority="High"
                ),

                BusinessRequirement(
                    requirement_id="BR-002",
                    description=(
                        "The system shall respond to appointment "
                        "requests within 2 seconds."
                    ),
                    requirement_type="Non-functional",
                    priority="High"
                ),

                BusinessRequirement(
                    requirement_id="BR-003",
                    description=(
                        "Only authenticated users shall be allowed "
                        "to access customer appointment records."
                    ),
                    requirement_type="Non-functional",
                    priority="High"
                ),

                BusinessRequirement(
                    requirement_id="BR-004",
                    description=(
                        "The system shall maintain 99.9% availability."
                    ),
                    requirement_type="Non-functional",
                    priority="High"
                )
            ]
        )
    )

    agent = NonFunctionalRequirementAgent()

    updated_state = agent.analyze(state)

    print("\n===== NON-FUNCTIONAL REQUIREMENTS =====")
    print(updated_state.non_functional_requirements)


if __name__ == "__main__":
    main()