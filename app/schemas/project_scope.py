from pydantic import BaseModel


class ProjectScope(BaseModel):
    in_scope: list[str]
    out_of_scope: list[str]