from pathlib import Path
import fitz


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from all pages of a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text from the PDF.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the provided file is not a PDF.
    """

    path = Path(file_path)

    # Check whether the file exists
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Make sure the file is actually a PDF
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file, received: {path.suffix}")

    text_parts = []

    # Open the PDF
    with fitz.open(path) as document:

        # Read every page
        for page in document:
            page_text = page.get_text()

            if page_text:
                text_parts.append(page_text)

    # Combine text from all pages
    extracted_text = "\n".join(text_parts)

    return extracted_text