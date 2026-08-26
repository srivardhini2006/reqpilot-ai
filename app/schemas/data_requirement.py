from pydantic import BaseModel


class DataEntity(BaseModel):
    entity_id: str
    source_requirement_id: str
    entity_name: str
    description: str
    attributes: list[str]
    relationships: list[str]


class DataRequirements(BaseModel):
    entities: list[DataEntity]