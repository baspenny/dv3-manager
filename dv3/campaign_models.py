from enum import Enum
from typing import Optional, List
import dv3
from pydantic import BaseModel


class CampaignFlight(BaseModel):
    plannedSpendAmountMicros: str
    plannedDates: dv3.DateRange


class ExternalBudgetSource(str, Enum):
    unspecified = "EXTERNAL_BUDGET_SOURCE_UNSPECIFIED"
    none = "EXTERNAL_BUDGET_SOURCE_NONE"
    mediaOcean = "EXTERNAL_BUDGET_SOURCE_MEDIA_OCEAN"


class PrismaType(str, Enum):
    unspecified = "PRISMA_TYPE_UNSPECIFIED"
    display = "PRISMA_TYPE_DISPLAY"
    search = "PRISMA_TYPE_SEARCH"
    video = "PRISMA_TYPE_VIDEO"
    audio = "PRISMA_TYPE_AUDIO"
    social = "PRISMA_TYPE_SOCIAL"
    fee = "PRISMA_TYPE_FEE"


class PrismaCpeCode(BaseModel):
    prismaClientCode: str
    prismaProductCode: str
    prismaEstimateCode: str


class PrismaConfig(BaseModel):
    prisma_type: PrismaType
    prisma_cpe_code: PrismaCpeCode
    supplier: str


class CampaignBudget(BaseModel):
    budgetId: str
    displayName: str
    budgetUnit: dv3.BudgetUnit
    budgetAmountMicros: str
    dateRange: dv3.DateRange
    externalBudgetSource: ExternalBudgetSource
    externalBudgetId: str
    invoiceGroupingId: str
    prismaConfig: PrismaConfig


class CampaignGoalType(str, Enum):
    unspecified = 'CAMPAIGN_GOAL_TYPE_UNSPECIFIED'
    appInstall = 'CAMPAIGN_GOAL_TYPE_APP_INSTALL'
    brandAwareness = 'CAMPAIGN_GOAL_TYPE_BRAND_AWARENESS'
    offlineAction = 'CAMPAIGN_GOAL_TYPE_OFFLINE_ACTION'
    onlineAction = 'CAMPAIGN_GOAL_TYPE_ONLINE_ACTION'


class PerformanceGoalType(str, Enum):
    unspecified = 'PERFORMANCE_GOAL_TYPE_UNSPECIFIED'
    cpm = 'PERFORMANCE_GOAL_TYPE_CPM'
    cpc = 'PERFORMANCE_GOAL_TYPE_CPC'
    cpa = 'PERFORMANCE_GOAL_TYPE_CPA'
    ctr = 'PERFORMANCE_GOAL_TYPE_CTR'
    viewability = 'PERFORMANCE_GOAL_TYPE_VIEWABILITY'
    cpiavc = 'PERFORMANCE_GOAL_TYPE_CPIAVC'
    cpe = 'PERFORMANCE_GOAL_TYPE_CPE'
    clickCvr = 'PERFORMANCE_GOAL_TYPE_CLICK_CVR'
    impressionCvr = 'PERFORMANCE_GOAL_TYPE_IMPRESSION_CVR'
    vcpm = 'PERFORMANCE_GOAL_TYPE_VCPM'
    vtr = 'PERFORMANCE_GOAL_TYPE_VTR'
    audioCompletionRate = 'PERFORMANCE_GOAL_TYPE_AUDIO_COMPLETION_RATE'
    videoCompletionRate = 'PERFORMANCE_GOAL_TYPE_VIDEO_COMPLETION_RATE'
    other = 'PERFORMANCE_GOAL_TYPE_OTHER'


class PerformanceGoal(BaseModel):
    performanceGoalType: PerformanceGoalType
    performanceGoalAmountMicros: str = None
    performanceGoalPercentageMicros: str = None
    performanceGoalString: str = None


class CampaignGoal(BaseModel):
    campaignGoalType: CampaignGoalType
    performanceGoal: PerformanceGoal


class Campaign(BaseModel):
    name: str
    advertiserId: str
    campaignId: str
    displayName: str
    entityStatus: dv3.EntityStatus
    updateTime: str
    campaignGoal: Optional[CampaignGoal]
    campaignFlight: Optional[CampaignFlight]
    frequencyCap: Optional[dv3.FrequencyCap]
    campaignBudgets: List[CampaignBudget]
