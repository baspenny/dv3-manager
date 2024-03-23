from enum import Enum
from pydantic import BaseModel


class EntityStatus(str, Enum):
    ACTIVE = "ENTITY_STATUS_ACTIVE"
    PAUSED = "PAUSED"
    ENTITY_STATUS_DRAFT = "ENTITY_STATUS_DRAFT"


class Date(BaseModel):
    year: int
    month: int
    day: int

class DateRange(BaseModel):
    startDate: Date
    endDate: Date



