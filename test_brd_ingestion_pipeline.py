from app.services.document_service import load_document
from app.ingestion.section_parser import parse_sections
from app.services.brd_state_service import create_brd_state


def main():

    file_path = "data/brds/full_sample_brd.docx"

    print("===== BRD INGESTION TEST =====")

    # 1. Load document
    print("\n1. Loading document...")

    raw_text = load_document(file_path)

    print("Document loaded successfully.")
    print(f"Extracted characters: {len(raw_text)}")

    # 2. Parse sections
    print("\n2. Parsing BRD sections...")

    sections = parse_sections(raw_text)

    print("Sections detected:")

    for section_name in sections:
        print(f"- {section_name}")

    # 3. Create BRDState
    print("\n3. Creating BRDState...")

    state = create_brd_state(
        raw_text,
        sections
    )

    print("BRDState created successfully.")

    # 4. Display important fields
    print("\n===== STATE SUMMARY =====")

    print(
        "Executive Summary:",
        bool(state.executive_summary)
    )

    print(
        "Project Objectives:",
        bool(state.project_objectives)
    )

    print(
        "Project Scope:",
        bool(state.project_scope)
    )

    print(
        "Business Requirements:",
        bool(state.business_requirements)
    )

    print(
        "Key Stakeholders:",
        bool(state.key_stakeholders)
    )

    print(
        "Project Constraints:",
        bool(state.project_constraints)
    )

    print(
        "Cost Benefit Analysis:",
        bool(state.cost_benefit_analysis)
    )

    print("\nBRD ingestion pipeline test completed.")


if __name__ == "__main__":
    main()