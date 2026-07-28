from app.ingestion.pdf_parser import extract_text_from_pdf


def main():
    try:
        text = extract_text_from_pdf("data/brds/sample_brd.pdf")

        print("===== EXTRACTED BRD =====")
        print(text)

    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()