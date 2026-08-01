from pathlib import Path

from app.ingestion.pdf_parser import extract_text_from_pdf
from app.ingestion.docx_parser import extract_text_from_docx


def load_document(file_path: str) -> str:
    """
    Load a BRD document and return its extracted text.
    Supports PDF and DOCX files.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return extract_text_from_pdf(file_path)

    elif suffix == ".docx":
        return extract_text_from_docx(file_path)

    else:
        raise ValueError(f"Unsupported file type: {suffix}")