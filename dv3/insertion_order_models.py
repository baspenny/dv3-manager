from typing import Optional
import dv3
from pydantic import BaseModel
from enum import Enum


class InsertionOrderBudget(BaseModel): ...  # Onvolledig, vul aan op basis van JSON-schema


class IntegrationDetails(BaseModel): ...  # Onvolledig, vul aan op basis van JSON-schema


class KpiType(str, Enum):
    """Mogelijke KPI-typen."""
    KPI_TYPE_UNSPECIFIED = "KPI_TYPE_UNSPECIFIED"  # Lowercase for consistency with enum members
    KPI_TYPE_CPM = "KPI_TYPE_CPM"
    KPI_TYPE_CPC = "KPI_TYPE_CPC"
    KPI_TYPE_CPA = "KPI_TYPE_CPA"
    KPI_TYPE_CTR = "KPI_TYPE_CTR"
    KPI_TYPE_VIEWABILITY = "KPI_TYPE_VIEWABILITY"
    KPI_TYPE_CPIAVC = "KPI_TYPE_CPIAVC"
    KPI_TYPE_CPE = "KPI_TYPE_CPE"
    KPI_TYPE_CLICK_CVR = "KPI_TYPE_CLICK_CVR"  # Combine words with uppercase first letter
    KPI_TYPE_IMPRESSION_CVR = "KPI_TYPE_IMPRESSION_CVR"
    KPI_TYPE_VCPM = "KPI_TYPE_VCPM"
    KPI_TYPE_VTR = "KPI_TYPE_VTR"
    KPI_TYPE_AUDIO_COMPLETION_RATE = "KPI_TYPE_AUDIO_COMPLETION_RATE"  # Combine words with uppercase first letter
    KPI_TYPE_VIDEO_COMPLETION_RATE = "KPI_TYPE_VIDEO_COMPLETION_RATE"
    KPI_TYPE_OTHER = "KPI_TYPE_OTHER"


class Kpi(BaseModel):
    kpiType: KpiType
    kpiValue: Optional[str] = None
    kpiPercentageMicros: Optional[str] = None
    kpiString: Optional[str] = None


class InsertionOrderType(Enum):
    INSERTION_ORDER_TYPE_UNSPECIFIED = "INSERTION_ORDER_TYPE_UNSPECIFIED"
    RTB = "RTB"
    OVER_THE_TOP = "OVER_THE_TOP"


class InsertionOrder(BaseModel):
    name: str
    advertiserId: str
    campaignId: str
    insertionOrderId: str
    displayName: str
    insertionOrderType: InsertionOrderType
    entityStatus: dv3.EntityStatus
    updateTime: str
    partnerCosts: list[dv3.PartnerCost]
    pacing: dv3.Pacing
    frequencyCap: dv3.FrequencyCap
    integrationDetails: IntegrationDetails
    kpi: Kpi
    budget: InsertionOrderBudget
    bidStrategy: dv3.BiddingStrategy
    reservationType: str
