from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)
from app.agents.conflict_agent import ConflictAgent


def main():

    state = BRDState(
        business_requirements_analysis=BusinessRequirements(
            requirements=[
                BusinessRequirement(
                    requirement_id="BR-001",
                    description="Customers can cancel appointments at any time.",
                    requirement_type="Business",
                    priority="High"
                ),
                BusinessRequirement(
                    requirement_id="BR-002",
                    description="Appointments cannot be cancelled within 24 hours of the appointment.",
                    requirement_type="Business",
                    priority="High"
                ),
                BusinessRequirement(
                    requirement_id="BR-003",
                    description="Customers can view available appointment slots.",
                    requirement_type="Functional",
                    priority="Medium"
                )
            ]
        )
    )

    agent = ConflictAgent()

    updated_state = agent.analyze(state)

    print("\n===== REQUIREMENT CONFLICTS =====")
    print(updated_state.conflicts)


if __name__ == "__main__":
    main()