from app.schemas.brd_state import BRDState
from app.schemas.fsd import FSDDocument


class FSDAssemblyAgent:

    def analyze(self, state: BRDState) -> BRDState:

        functional_requirements = []

        if state.functional_requirements:
            functional_requirements = (
                state.functional_requirements.requirements
            )

        use_cases = []

        if state.use_cases:
            use_cases = state.use_cases.use_cases

        business_rules = []

        if state.business_rules:
            business_rules = state.business_rules.rules

        data_requirements = []

        if state.data_requirements:
            data_requirements = state.data_requirements.entities

        non_functional_requirements = []

        if state.non_functional_requirements:
            non_functional_requirements = (
                state.non_functional_requirements.requirements
            )

        traceability_matrix = []

        if state.traceability_matrix:
            traceability_matrix = state.traceability_matrix.traces

        title = "Functional Specification Document"

        introduction = (
            "This Functional Specification Document describes the "
            "functional behavior, business rules, data requirements, "
            "non-functional requirements, and traceability derived "
            "from the validated Business Requirements Document."
        )

        business_context = ""

        if state.business_context:
            business_context = str(state.business_context)

        state.fsd = FSDDocument(
            title=title,
            introduction=introduction,
            business_context=business_context,
            functional_requirements=functional_requirements,
            use_cases=use_cases,
            business_rules=business_rules,
            data_requirements=data_requirements,
            non_functional_requirements=non_functional_requirements,
            traceability_matrix=traceability_matrix
        )

        return state