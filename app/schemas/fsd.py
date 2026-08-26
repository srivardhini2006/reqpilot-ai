from pydantic import BaseModel


class FSDDocument(BaseModel):
    title: str
    introduction: str
    business_context: str
    functional_requirements: list
    use_cases: list
    business_rules: list
    data_requirements: list
    non_functional_requirements: list
    traceability_matrix: list