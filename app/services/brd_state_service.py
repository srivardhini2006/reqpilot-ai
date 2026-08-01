from app.schemas.brd_state import BRDState


def create_brd_state(raw_text: str, sections: dict) -> BRDState:

    state = BRDState(
        raw_text=raw_text,

        executive_summary=sections.get("executive_summary", ""),

        project_objectives=sections.get("project_objectives", ""),

        project_scope=sections.get("project_scope", ""),

        business_requirements=sections.get("business_requirements", ""),

        key_stakeholders=sections.get("key_stakeholders", ""),

        project_constraints=sections.get("project_constraints", ""),

        cost_benefit_analysis=sections.get("cost_benefit_analysis", ""),
    )

    return state