from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)
from app.agents.ambiguity_agent import AmbiguityAgent


def main():

    state = BRDState(
        business_requirements_analysis=BusinessRequirements(
            requirements=[
                BusinessRequirement(
                    requirement_id="BR-001",
                    description="The system shall respond quickly to user requests.",
                    requirement_type="Functional",
                    priority="High"
                ),
                BusinessRequirement(
                    requirement_id="BR-002",
                    description="The system shall allow users to book appointments online.",
                    requirement_type="Functional",
                    priority="High"
                )
            ]
        )
    )

    agent = AmbiguityAgent()

    updated_state = agent.analyze(state)

    print("\n===== AMBIGUITIES =====")
    print(updated_state.ambiguities)


if __name__ == "__main__":
    main()