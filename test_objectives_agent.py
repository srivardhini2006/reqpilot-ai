from app.schemas.brd_state import BRDState
from app.agents.objectives_agent import ObjectivesAgent


def main():

    state = BRDState(
        project_objectives="""
        1. Reduce appointment waiting time.
        2. Improve patient satisfaction.
        3. Reduce manual work for hospital staff.
        4. Increase online appointment adoption.
        """
    )

    agent = ObjectivesAgent()

    updated_state = agent.analyze(state)

    print("\n===== PROJECT OBJECTIVES =====")
    print(updated_state.project_objectives_analysis)


if __name__ == "__main__":
    main()