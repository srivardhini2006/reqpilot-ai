from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)

from app.pipeline.reqpilot_pipeline import ReqPilotPipeline


def main():

    state = BRDState(
        business_requirements_analysis=BusinessRequirements(
            requirements=[
                BusinessRequirement(
                    requirement_id="BR-001",
                    description=(
                        "The system shall allow registered customers "
                        "to book available appointment slots online."
                    ),
                    requirement_type="Functional",
                    priority="High"
                ),
                BusinessRequirement(
                    requirement_id="BR-002",
                    description=(
                        "The system shall allow customers to cancel "
                        "appointments more than 24 hours before "
                        "the scheduled appointment."
                    ),
                    requirement_type="Functional",
                    priority="High"
                )
            ]
        )
    )

    pipeline = ReqPilotPipeline()

    final_state = pipeline.run(state)

    print("\n========================================")
    print("REQPILOT PIPELINE COMPLETED")
    print("========================================")

    print("\nFunctional Requirements:")
    print(final_state.functional_requirements)

    print("\nUse Cases:")
    print(final_state.use_cases)

    print("\nBusiness Rules:")
    print(final_state.business_rules)

    print("\nData Requirements:")
    print(final_state.data_requirements)

    print("\nNon-Functional Requirements:")
    print(final_state.non_functional_requirements)

    print("\nTraceability:")
    print(final_state.traceability_matrix)

    print("\nFSD:")
    print(final_state.fsd)

    print("\nTest Scenarios:")
    print(final_state.test_scenarios)

    print("\nTest Cases:")
    print(final_state.test_cases)

    print("\nTest Traceability:")
    print(final_state.test_traceability)


if __name__ == "__main__":
    main()