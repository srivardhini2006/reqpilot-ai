from pydantic import BaseModel


class BusinessRule(BaseModel):
    rule_id: str
    source_requirement_id: str
    rule_description: str
    condition: str
    expected_behavior: str


class BusinessRules(BaseModel):
    rules: list[BusinessRule]