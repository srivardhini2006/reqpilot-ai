from app.schemas.brd_state import BRDState
from app.agents.scope_agent import ScopeAgent


def main():

    state = BRDState(
        project_scope="""
        In Scope:
        - Online appointment booking
        - Appointment cancellation
        - Doctor availability viewing

        Out of Scope:
        - Online payment
        - Insurance processing
        - Pharmacy management
        """
    )

    agent = ScopeAgent()

    updated_state = agent.analyze(state)

    print("\n===== PROJECT SCOPE =====")
    print(updated_state.project_scope_analysis)


if __name__ == "__main__":
    main()