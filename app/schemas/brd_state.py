from pydantic import BaseModel

from app.schemas.business_context import BusinessContext
from app.schemas.project_objectives import ProjectObjectives
from app.schemas.project_scope import ProjectScope
from app.schemas.business_requirement import BusinessRequirements
from app.schemas.ambiguity import Ambiguities
from app.schemas.gap import Gaps
from app.schemas.conflict import Conflicts
from app.schemas.clarification_question import ClarificationQuestions
from app.schemas.requirement_validation import RequirementValidations
from app.schemas.requirement_classification import RequirementClassifications
from app.schemas.requirement_priority import RequirementPriorities
from app.schemas.traceability import RequirementTraces


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

    ambiguities: Ambiguities | None = None
    gaps: Gaps | None = None
    conflicts: Conflicts | None = None
    clarification_questions: ClarificationQuestions | None = None

    validation_report: RequirementValidations | None = None
    requirement_classifications: RequirementClassifications | None = None
    requirement_priorities: RequirementPriorities | None = None

    traceability_matrix: RequirementTraces | None = None