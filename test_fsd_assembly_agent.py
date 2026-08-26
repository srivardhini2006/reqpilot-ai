from app.schemas.brd_state import BRDState

from app.schemas.functional_requirement import (
    FunctionalRequirements,
    FunctionalRequirement
)

from app.schemas.use_case import (
    UseCases,
    UseCase
)

from app.schemas.business_rule import (
    BusinessRules,
    BusinessRule
)

from app.schemas.data_requirement import (
    DataRequirements,
    DataEntity
)

from app.schemas.non_functional_requirement import (
    NonFunctionalRequirements,
    NonFunctionalRequirement
)

from app.schemas.traceability import (
    RequirementTraces,
    RequirementTrace
)

from app.agents.fsd_assembly_agent import FSDAssemblyAgent


def main():

    state = BRDState(

        functional_requirements=FunctionalRequirements(
            requirements=[
                FunctionalRequirement(
                    functional_requirement_id="FR-001",
                    source_requirement_id="BR-001",
                    title="Appointment Booking",
                    description="Customers can book appointments.",
                    actor="Customer",
                    preconditions=[
                        "Customer is registered."
                    ],
                    main_flow=[
                        "Customer selects an appointment slot.",
                        "System creates the appointment."
                    ],
                    expected_result="Appointment is successfully created."
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
                        "Customer selects appointment.",
                        "System confirms appointment."
                    ],
                    alternative_flows=[
                        "Selected appointment slot is unavailable."
                    ],
                    postconditions=[
                        "Appointment is created."
                    ]
                )
            ]
        ),

        business_rules=BusinessRules(
            rules=[
                BusinessRule(
                    rule_id="BRULE-001",
                    source_requirement_id="BR-001",
                    rule_description="Only available slots can be booked.",
                    condition="Selected slot is available.",
                    expected_behavior="System permits booking."
                )
            ]
        ),

        data_requirements=DataRequirements(
            entities=[
                DataEntity(
                    entity_id="ENT-001",
                    source_requirement_id="BR-001",
                    entity_name="Appointment",
                    description="Represents a customer appointment.",
                    attributes=[
                        "appointment_id",
                        "appointment_date",
                        "status"
                    ],
                    relationships=[
                        "Belongs to Customer"
                    ]
                )
            ]
        ),

        non_functional_requirements=NonFunctionalRequirements(
            requirements=[
                NonFunctionalRequirement(
                    nfr_id="NFR-001",
                    source_requirement_id="BR-001",
                    category="Performance",
                    description="Booking requests should be processed quickly.",
                    measurable_criteria="Response time requirement to be confirmed."
                )
            ]
        ),

        traceability_matrix=RequirementTraces(
            traces=[
                RequirementTrace(
                    business_requirement_id="BR-001",
                    functional_requirement_id="FR-001",
                    use_case_id="UC-001",
                    test_case_id=None
                )
            ]
        )
    )

    agent = FSDAssemblyAgent()

    updated_state = agent.analyze(state)

    print("\n===== FSD DOCUMENT =====")
    print(updated_state.fsd)


if __name__ == "__main__":
    main()