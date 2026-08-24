from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)

from app.agents.functional_requirement_agent import (
    FunctionalRequirementAgent
)


def main():

    state = BRDState(
        business_requirements_analysis=BusinessRequirements(
            requirements=[
                BusinessRequirement(
                    requirement_id="BR-001",
                    description=(
                        "The system shall allow registered customers "
                        "to book available appointment slots."
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
                )
            ]
        )
    )

    agent = FunctionalRequirementAgent()

    updated_state = agent.analyze(state)

    print("\n===== FUNCTIONAL REQUIREMENTS =====")
    print(updated_state.functional_requirements)


if __name__ == "__main__":
    main()