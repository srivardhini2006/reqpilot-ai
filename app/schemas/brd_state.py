from pydantic import BaseModel, Field
from app.schemas.business_context import BusinessContext
from app.schemas.project_objectives import ProjectObjectives
from app.schemas.project_scope import ProjectScope
from app.schemas.business_requirement import BusinessRequirements
from app.schemas.ambiguity import Ambiguities


class BRDState(BaseModel):

    raw_text: str = ""

    executive_summary: str = ""
    project_objectives: str = ""
    project_scope: str = ""
    business_requirements: str = ""
    key_stakeholders: str = ""
    project_constraints: str = ""
    cost_benefit_analysis: str = ""

    business_context: BusinessContext | None = None

    project_objectives_analysis: ProjectObjectives | None = None

    project_scope_analysis: ProjectScope | None = None

    business_requirements_analysis: BusinessRequirements | None = None

    extracted_requirements: list = Field(default_factory=list)

    ambiguities: list = Field(default_factory=list)

    gaps: list = Field(default_factory=list)

    conflicts: list = Field(default_factory=list)

    clarification_questions: list = Field(default_factory=list)

    functional_requirements: list = Field(default_factory=list)

    validation_report: dict = Field(default_factory=dict)

    fsd: dict = Field(default_factory=dict)