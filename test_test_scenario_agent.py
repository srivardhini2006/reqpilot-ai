from app.schemas.brd_state import BRDState

from app.schemas.functional_requirement import (
    FunctionalRequirements,
    FunctionalRequirement
)

from app.schemas.use_case import (
    UseCases,
    UseCase
)

from app.agents.test_scenario_agent import TestScenarioAgent


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
                        "Customer selects an available slot.",
                        "System validates the slot.",
                        "System creates the appointment."
                    ],
                    expected_result=(
                        "Appointment is successfully created."
                    )
                )
            ]
        ),

        use_cases=UseCases(
            use_cases=[
                UseCase(
                    use_case_id="UC-001",
                    functional_requirement_id="FR-001",
                    title="Book Appointment",
                    actor="Customer",
                    preconditions=[
                        "Customer is registered."
                    ],
                    main_flow=[
                        "Customer selects an appointment slot.",
                        "System validates the slot.",
                        "System creates the appointment."
                    ],
                    alternative_flows=[
                        "Selected slot is unavailable."
                    ],
                    postconditions=[
                        "Appointment is created."
                    ]
                )
            ]
        )
    )

    agent = TestScenarioAgent()

    updated_state = agent.analyze(state)

    print("\n===== TEST SCENARIOS =====")
    print(updated_state.test_scenarios)


if __name__ == "__main__":
    main()