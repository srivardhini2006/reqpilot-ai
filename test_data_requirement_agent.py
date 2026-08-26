from app.schemas.brd_state import BRDState
from app.schemas.functional_requirement import (
    FunctionalRequirements,
    FunctionalRequirement
)

from app.agents.data_requirement_agent import DataRequirementAgent


def main():

    state = BRDState(
        functional_requirements=FunctionalRequirements(
            requirements=[
                FunctionalRequirement(
                    functional_requirement_id="FR-001",
                    source_requirement_id="BR-001",
                    title="Appointment Booking",
                    description=(
                        "The system shall allow registered customers "
                        "to book available appointment slots."
                    ),
                    actor="Customer",
                    preconditions=[
                        "Customer is registered.",
                        "Appointment slot is available."
                    ],
                    main_flow=[
                        "Customer selects an appointment slot.",
                        "System validates the selected slot.",
                        "System creates the appointment."
                    ],
                    expected_result=(
                        "The appointment is successfully created."
                    )
                )
            ]
        )
    )

    agent = DataRequirementAgent()

    updated_state = agent.analyze(state)

    print("\n===== DATA REQUIREMENTS =====")
    print(updated_state.data_requirements)


if __name__ == "__main__":
    main()