from app.schemas.brd_state import BRDState
from app.schemas.business_requirement import (
    BusinessRequirements,
    BusinessRequirement
)
from app.schemas.business_context import BusinessContext
from app.schemas.project_objectives import ProjectObjectives

from app.agents.prioritization_agent import PrioritizationAgent


def main():

    state = BRDState(

        business_context=BusinessContext(
            domain="Healthcare",
            business_problem="Long patient waiting times",
            proposed_solution="Online appointment booking system",
            business_goal="Reduce appointment waiting time",
            expected_benefits=[
                "Reduced waiting time",
                "Improved patient experience"
            ]
        ),

        project_objectives_analysis=ProjectObjectives(
            objectives=[
                "Reduce appointment waiting time",
                "Improve patient satisfaction"
            ]
        ),

        business_requirements_analysis=BusinessRequirements(
            requirements=[
                BusinessRequirement(
                    requirement_id="BR-001",
                    description=(
                        "The system shall allow customers "
                        "to book appointments online."
                    ),
                    requirement_type="Functional",
                    priority="High"
                ),

                BusinessRequirement(
                    requirement_id="BR-002",
                    description=(
                        "The system shall send appointment "
                        "confirmation notifications."
                    ),
                    requirement_type="Functional",
                    priority="Medium"
                ),

                BusinessRequirement(
                    requirement_id="BR-003",
                    description=(
                        "The system shall allow users to "
                        "upload a profile picture."
                    ),
                    requirement_type="Functional",
                    priority="Low"
                )
            ]
        )
    )

    agent = PrioritizationAgent()

    updated_state = agent.analyze(state)

    print("\n===== REQUIREMENT PRIORITIES =====")
    print(updated_state.requirement_priorities)


if __name__ == "__main__":
    main()