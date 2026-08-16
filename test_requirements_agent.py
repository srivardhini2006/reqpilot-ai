from app.schemas.brd_state import BRDState
from app.agents.requirements_agent import RequirementsAgent


def main():

    state = BRDState(
        business_requirements="""
        BR-001: The system shall allow customers to book
        appointments online.

        BR-002: The system shall allow customers to cancel
        appointments.

        BR-003: The system shall send confirmation notifications
        to customers.

        BR-004: Administrators shall be able to manage doctor
        availability.
        """
    )

    agent = RequirementsAgent()

    updated_state = agent.analyze(state)

    print("\n===== BUSINESS REQUIREMENTS =====")
    print(updated_state.business_requirements_analysis)


if __name__ == "__main__":
    main()