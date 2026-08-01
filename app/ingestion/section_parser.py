import re


SECTION_HEADERS = [
    "Executive Summary",
    "Project Objectives",
    "Project Scope",
    "Business Requirements",
    "Key Stakeholders",
    "Project Constraints",
    "Cost Benefit Analysis",
]


def parse_sections(text: str) -> dict:
    """
    Parse a BRD into predefined sections.
    """

    sections = {}

    # Create one regex that matches any heading
    pattern = "|".join(re.escape(header) for header in SECTION_HEADERS)

    matches = list(re.finditer(pattern, text, flags=re.IGNORECASE))

    for i, match in enumerate(matches):

        section_name = match.group(0)

        start = match.end()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        content = text[start:end].strip()

        key = section_name.lower().replace(" ", "_")

        sections[key] = content

    return sections