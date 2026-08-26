from app.schemas.brd_state import BRDState
from app.schemas.functional_requirement import (
    FunctionalRequirements,
    FunctionalRequirement
)

from app.agents.business_rule_agent import BusinessRuleAgent


def main():

    state = BRDState(
        functional_requirements=FunctionalRequirements(
            requirements=[
                FunctionalRequirement(
                    functional_requirement_id="FR-001",
                    source_requirement_id="BR-001",
                    title="Appointment Cancellation",
                    description=(
                        "The system shall allow customers to cancel "
                        "appointments. Appointments cannot be cancelled "
                        "within 24 hours of the scheduled appointment."
                    ),
                    actor="Customer",
                    preconditions=[
                        "Customer has an existing appointment."
                    ],
                    main_flow=[
                        "Customer selects an existing appointment.",
                        "Customer requests cancellation.",
                        "System validates the cancellation request.",
                        "System cancels the appointment."
                    ],
                    expected_result=(
                        "The appointment is successfully cancelled."
                    )
                )
            ]
        )
    )

    agent = BusinessRuleAgent()

    updated_state = agent.analyze(state)

    print("\n===== BUSINESS RULES =====")
    print(updated_state.business_rules)


if __name__ == "__main__":
    main()