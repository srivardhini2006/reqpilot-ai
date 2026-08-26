from app.schemas.brd_state import BRDState
from app.schemas.test_scenario import (
    TestScenarios,
    TestScenario
)

from app.agents.test_case_agent import TestCaseAgent


def main():

    state = BRDState(

        test_scenarios=TestScenarios(
            scenarios=[
                TestScenario(
                    scenario_id="TS-001",
                    source_functional_requirement_id="FR-001",
                    source_use_case_id="UC-001",
                    title="Successfully book an available appointment",
                    description=(
                        "Verify that a registered customer can "
                        "successfully book an available appointment."
                    ),
                    scenario_type="Positive"
                ),

                TestScenario(
                    scenario_id="TS-002",
                    source_functional_requirement_id="FR-001",
                    source_use_case_id="UC-001",
                    title="Attempt to book unavailable appointment",
                    description=(
                        "Verify that the system prevents booking "
                        "when the selected slot is unavailable."
                    ),
                    scenario_type="Negative"
                )
            ]
        )
    )

    agent = TestCaseAgent()

    updated_state = agent.analyze(state)

    print("\n===== TEST CASES =====")
    print(updated_state.test_cases)


if __name__ == "__main__":
    main()