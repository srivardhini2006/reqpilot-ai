from app.schemas.brd_state import BRDState
from app.schemas.test_traceability import TestTraceability


class TestTraceabilityAgent:

    def analyze(self, state: BRDState) -> BRDState:

        if not state.test_cases:
            return state

        traces = []

        # Build lookup for functional requirements
        functional_requirement_lookup = {}

        if state.functional_requirements:
            for requirement in state.functional_requirements.requirements:
                functional_requirement_lookup[
                    requirement.functional_requirement_id
                ] = requirement.source_requirement_id

        # Build lookup for use cases
        use_case_lookup = {}

        if state.use_cases:
            for use_case in state.use_cases.use_cases:
                use_case_lookup[
                    use_case.functional_requirement_id
                ] = use_case.use_case_id

        # Build lookup for test scenarios
        scenario_lookup = {}

        if state.test_scenarios:
            for scenario in state.test_scenarios.scenarios:
                scenario_lookup[
                    scenario.scenario_id
                ] = scenario

        # Build final traceability
        for test_case in state.test_cases.test_cases:

            functional_requirement_id = (
                test_case.source_functional_requirement_id
            )

            business_requirement_id = (
                functional_requirement_lookup.get(
                    functional_requirement_id
                )
            )

            scenario = scenario_lookup.get(
                test_case.source_scenario_id
            )

            use_case_id = None

            if scenario:
                use_case_id = scenario.source_use_case_id

            if business_requirement_id:

                traces.append(
                    {
                        "business_requirement_id":
                            business_requirement_id,

                        "functional_requirement_id":
                            functional_requirement_id,

                        "use_case_id":
                            use_case_id,

                        "scenario_id":
                            test_case.source_scenario_id,

                        "test_case_id":
                            test_case.test_case_id
                    }
                )

        state.test_traceability = TestTraceability(
            traces=traces
        )

        return state