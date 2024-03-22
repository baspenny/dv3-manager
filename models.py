from pydantic import BaseModel
from enum import Enum


class EntityStatus(str, Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    ENTITY_STATUS_DRAFT = "ENTITY_STATUS_DRAFT"


class LineItem(BaseModel):
    id: str
    advertiserId: str
    entityStatus: EntityStatus


class LineItemUpdate(BaseModel):
    lineItems: list[LineItem]
