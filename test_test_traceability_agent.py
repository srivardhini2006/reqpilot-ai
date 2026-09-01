from app.schemas.brd_state import BRDState

from app.schemas.functional_requirement import (
    FunctionalRequirements,
    FunctionalRequirement
)

from app.schemas.use_case import (
    UseCases,
    UseCase
)

from app.schemas.test_scenario import (
    TestScenarios,
    TestScenario
)

from app.schemas.test_case import (
    TestCases,
    TestCase
)

from app.agents.test_traceability_agent import (
    TestTraceabilityAgent
)


def main():

    state = BRDState(

        functional_requirements=FunctionalRequirements(
            requirements=[
                FunctionalRequirement(
                    functional_requirement_id="FR-001",
                    source_requirement_id="BR-001",
                    title="Appointment Booking",
                    description=(
                        "Customers can book available appointments."
                    ),
                    actor="Customer",
                    preconditions=[
                        "Customer is registered."
                    ],
                    main_flow=[
                        "Customer selects an appointment.",
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
                        "Customer selects an appointment.",
                        "System creates the appointment."
                    ],
                    alternative_flows=[],
                    postconditions=[
                        "Appointment is created."
                    ]
                )
            ]
        ),

        test_scenarios=TestScenarios(
            scenarios=[
                TestScenario(
                    scenario_id="TS-001",
                    source_functional_requirement_id="FR-001",
                    source_use_case_id="UC-001",
                    title="Successfully book appointment",
                    description=(
                        "Verify successful appointment booking."
                    ),
                    scenario_type="Positive"
                )
            ]
        ),

        test_cases=TestCases(
            test_cases=[
                TestCase(
                    test_case_id="TC-001",
                    source_scenario_id="TS-001",
                    source_functional_requirement_id="FR-001",
                    title="Book available appointment",
                    test_type="Positive",
                    preconditions=[
                        "Customer is registered.",
                        "Appointment is available."
                    ],
                    test_steps=[
                        "Login as customer.",
                        "Select available appointment.",
                        "Confirm booking."
                    ],
                    expected_results=[
                        "Appointment is successfully created."
                    ]
                )
            ]
        )
    )

    agent = TestTraceabilityAgent()

    updated_state = agent.analyze(state)

    print("\n===== TEST TRACEABILITY =====")
    print(updated_state.test_traceability)


if __name__ == "__main__":
    main()