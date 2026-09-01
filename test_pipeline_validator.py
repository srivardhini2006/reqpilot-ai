from app.schemas.brd_state import BRDState
from app.schemas.functional_requirement import (
    FunctionalRequirements,
    FunctionalRequirement
)
from app.schemas.use_case import (
    UseCases,
    UseCase
)

from app.validators.pipeline_validator import PipelineValidator


def main():

    state = BRDState(

        functional_requirements=FunctionalRequirements(
            requirements=[
                FunctionalRequirement(
                    functional_requirement_id="FR-001",
                    source_requirement_id="BR-001",
                    title="Book Appointment",
                    description="Customer can book an appointment.",
                    actor="Customer",
                    preconditions=[
                        "Customer is registered."
                    ],
                    main_flow=[
                        "Customer selects appointment.",
                        "System confirms booking."
                    ],
                    expected_result="Appointment is booked."
                )
            ]
        ),

        use_cases=UseCases(
            use_cases=[
                UseCase(
                    use_case_id="UC-001",

                    # CORRECT REFERENCE
                    functional_requirement_id="FR-001",

                    title="Book Appointment",
                    actor="Customer",
                    preconditions=[
                        "Customer is registered."
                    ],
                    main_flow=[
                        "Customer books appointment."
                    ],
                    alternative_flows=[],
                    postconditions=[
                        "Appointment is booked."
                    ]
                )
            ]
        )
    )

    validator = PipelineValidator()

    errors = validator.validate_consistency(state)

    print("\n===== VALID STATE TEST =====")

    if errors:

        print("ERROR: Valid state produced validation errors.")

        for error in errors:
            print("-", error)

    else:

        print("Validation PASSED.")
        print("All available references are valid.")


if __name__ == "__main__":
    main()