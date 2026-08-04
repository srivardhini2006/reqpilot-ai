from typing import List
from pydantic import BaseModel


class BusinessContext(BaseModel):
    """
    Represents the business understanding extracted
    from the Executive Summary of a BRD.
    """

    domain: str

    business_problem: str

    proposed_solution: str

    business_goal: str

    expected_benefits: List[str]