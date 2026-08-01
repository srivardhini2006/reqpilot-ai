from app.services.document_service import load_document
from app.ingestion.section_parser import parse_sections
from app.services.brd_state_service import create_brd_state
import json

def main():

    raw_text = load_document("data/brds/sample_brd.pdf")

    sections = parse_sections(raw_text)

    state = create_brd_state(raw_text, sections)

    print(json.dumps(state.model_dump(), indent=4))


if __name__ == "__main__":
    main()