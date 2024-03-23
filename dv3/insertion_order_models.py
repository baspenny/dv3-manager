from typing import Optional
import dv3
from pydantic import BaseModel
from enum import Enum


class InsertionOrderBudget(BaseModel): ...  # Onvolledig, vul aan op basis van JSON-schema


class IntegrationDetails(BaseModel): ...  # Onvolledig, vul aan op basis van JSON-schema


class KpiType(str, Enum):
    """Mogelijke KPI-typen."""
    unspecified = "KPI_TYPE_UNSPECIFIED"  # Lowercase for consistency with enum members
    cpm = "KPI_TYPE_CPM"
    cpc = "KPI_TYPE_CPC"
    cpa = "KPI_TYPE_CPA"
    ctr = "KPI_TYPE_CTR"
    viewability = "KPI_TYPE_VIEWABILITY"
    cpiavc = "KPI_TYPE_CPIAVC"
    cpe = "KPI_TYPE_CPE"
    clickCvr = "KPI_TYPE_CLICK_CVR"  # Combine words with uppercase first letter
    impressionCvr = "KPI_TYPE_IMPRESSION_CVR"
    vcpm = "KPI_TYPE_VCPM"
    vtr = "KPI_TYPE_VTR"
    audioCompletionRate = "KPI_TYPE_AUDIO_COMPLETION_RATE"  # Combine words with uppercase first letter
    videoCompletionRate = "KPI_TYPE_VIDEO_COMPLETION_RATE"
    other = "KPI_TYPE_OTHER"


class Kpi(BaseModel):
    kpiType: KpiType
    kpiValue: Optional[str] = None
    kpiPercentageMicros: Optional[str] = None
    kpiString: Optional[str] = None


class InsertionOrderType(Enum):
    UNSPECIFIED = "INSERTION_ORDER_TYPE_UNSPECIFIED"
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
