from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)
from app.agents.gap_agent import GapAgent


def main():

    state = BRDState(
        business_requirements_analysis=BusinessRequirements(
            requirements=[
                BusinessRequirement(
                    requirement_id="BR-001",
                    description="The system shall allow users to make online payments.",
                    requirement_type="Functional",
                    priority="High"
                ),
                BusinessRequirement(
                    requirement_id="BR-002",
                    description="The system shall allow customers to book appointments online.",
                    requirement_type="Functional",
                    priority="High"
                )
            ]
        )
    )

    agent = GapAgent()

    updated_state = agent.analyze(state)

    print("\n===== REQUIREMENT GAPS =====")
    print(updated_state.gaps)


if __name__ == "__main__":
    main()