class PipelineValidator:

    def validate_completeness(self, state):

        errors = []

        required_sections = {
            "functional_requirements":
                state.functional_requirements,

            "use_cases":
                state.use_cases,

            "business_rules":
                state.business_rules,

            "data_requirements":
                state.data_requirements,

            "non_functional_requirements":
                state.non_functional_requirements,

            "traceability_matrix":
                state.traceability_matrix,

            "fsd":
                state.fsd,

            "test_scenarios":
                state.test_scenarios,

            "test_cases":
                state.test_cases,

            "test_traceability":
                state.test_traceability,
        }

        for name, value in required_sections.items():

            if not value:

                errors.append(
                    f"{name} is missing."
                )

        return errors

    def validate_consistency(self, state):

        errors = []

        # --------------------------------
        # Build available IDs
        # --------------------------------

        functional_ids = set()
        use_case_ids = set()
        scenario_ids = set()
        test_case_ids = set()

        if state.functional_requirements:

            functional_ids = {
                req.functional_requirement_id
                for req in
                state.functional_requirements.requirements
            }

        if state.use_cases:

            use_case_ids = {
                uc.use_case_id
                for uc in
                state.use_cases.use_cases
            }

        if state.test_scenarios:

            scenario_ids = {
                scenario.scenario_id
                for scenario in
                state.test_scenarios.scenarios
            }

        if state.test_cases:

            test_case_ids = {
                tc.test_case_id
                for tc in
                state.test_cases.test_cases
            }

        # --------------------------------
        # Use Case → Functional Requirement
        # --------------------------------

        if state.use_cases:

            for use_case in state.use_cases.use_cases:

                if (
                    use_case.functional_requirement_id
                    not in functional_ids
                ):

                    errors.append(
                        f"{use_case.use_case_id} references "
                        f"missing functional requirement "
                        f"{use_case.functional_requirement_id}."
                    )

        # --------------------------------
        # Test Scenario → Functional Requirement
        # --------------------------------

        if state.test_scenarios:

            for scenario in state.test_scenarios.scenarios:

                if (
                    scenario.source_functional_requirement_id
                    not in functional_ids
                ):

                    errors.append(
                        f"{scenario.scenario_id} references "
                        f"missing functional requirement "
                        f"{scenario.source_functional_requirement_id}."
                    )

        # --------------------------------
        # Test Case → Test Scenario
        # --------------------------------

        if state.test_cases:

            for test_case in state.test_cases.test_cases:

                if (
                    test_case.source_scenario_id
                    not in scenario_ids
                ):

                    errors.append(
                        f"{test_case.test_case_id} references "
                        f"missing scenario "
                        f"{test_case.source_scenario_id}."
                    )

        # --------------------------------
        # Test Case → Functional Requirement
        # --------------------------------

        if state.test_cases:

            for test_case in state.test_cases.test_cases:

                if (
                    test_case.source_functional_requirement_id
                    not in functional_ids
                ):

                    errors.append(
                        f"{test_case.test_case_id} references "
                        f"missing functional requirement "
                        f"{test_case.source_functional_requirement_id}."
                    )

        return errors

    def validate(self, state):

        errors = []

        errors.extend(
            self.validate_completeness(state)
        )

        errors.extend(
            self.validate_consistency(state)
        )

        return errors