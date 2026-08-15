from app.schemas.brd_state import BRDState
from app.agents.executive_summary_agent import ExecutiveSummaryAgent


def main():

    state = BRDState(
        executive_summary="""
        ABC Hospital wants to develop an online appointment
        booking system to reduce patient waiting time and
        improve the patient experience.
        """
    )

    agent = ExecutiveSummaryAgent()

    updated_state = agent.analyze(state)

    print("\n===== BUSINESS CONTEXT =====")
    print(updated_state.business_context)


if __name__ == "__main__":
    main()