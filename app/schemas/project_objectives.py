from pydantic import BaseModel


class ProjectObjectives(BaseModel):
    objectives: list[str]