from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
import dv3


class LineItemFlightDateType(str, Enum):
    unspecified = "LINE_ITEM_FLIGHT_DATE_TYPE_UNSPECIFIED"
    inherited = "LINE_ITEM_FLIGHT_DATE_TYPE_INHERITED"
    custom = "LINE_ITEM_FLIGHT_DATE_TYPE_CUSTOM"


class LineItemFlight(BaseModel):
    flightDateType: LineItemFlightDateType
    dateRange: dv3.DateRange


class LineItemBudgetAllocationType(str, Enum):
    unspecified = "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNSPECIFIED"
    automatic = "LINE_ITEM_BUDGET_ALLOCATION_TYPE_AUTOMATIC"
    fixed = "LINE_ITEM_BUDGET_ALLOCATION_TYPE_FIXED"
    unlimited = "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNLIMITED"


class LineItemBudget(BaseModel):
    budgetAllocationType: Optional[LineItemBudgetAllocationType] = None
    budgetUnit: Optional[dv3.BudgetUnit] = None
    maxAmount: str = ''


class AudienceExpansionLevel(str, Enum):
    unknown = "UNKNOWN"
    noReach = "NO_REACH"
    leastReach = "LEAST_REACH"
    midReach = "MID_REACH"
    mostReach = "MOST_REACH"


class TargetingExpansionConfig(BaseModel):
    enableOptimizedTargeting: Optional[bool] = None
    audienceExpansionSeedListExcluded: Optional[bool] = None
    audienceExpansionLevel: Optional[AudienceExpansionLevel] = None


class Platform(str, Enum):
    unspecified = 'PLATFORM_UNSPECIFIED'
    iOS = 'IOS'
    android = 'ANDROID'


class MobileApp(BaseModel):
    appId: str
    platform: Platform
    displayName: str
    publisher: str


class LineItemWarningMessage(str, Enum):
    unspecified = "LINE_ITEM_WARNING_MESSAGE_UNSPECIFIED"
    invalidFlightDates = "INVALID_FLIGHT_DATES"
    expired = "EXPIRED"
    pendingFlight = "PENDING_FLIGHT"
    allPartnerEnabledExchangesNegativelyTargeted = "ALL_PARTNER_ENABLED_EXCHANGES_NEGATIVELY_TARGETED"
    invalidInventorySource = "INVALID_INVENTORY_SOURCE"
    appInventoryInvalidSiteTargeting = "APP_INVENTORY_INVALID_SITE_TARGETING"
    appInventoryInvalidAudienceLists = "APP_INVENTORY_INVALID_AUDIENCE_LISTS"
    noValidCreative = "NO_VALID_CREATIVE"
    parentInsertionOrderPaused = "PARENT_INSERTION_ORDER_PAUSED"
    parentInsertionOrderExpired = "PARENT_INSERTION_ORDER_EXPIRED"


class LineItemType(str, Enum):
    unspecified = "LINE_ITEM_TYPE_UNSPECIFIED"
    displayDefault = "LINE_ITEM_TYPE_DISPLAY_DEFAULT"
    displayMobileAppInstall = "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INSTALL"
    videoDefault = "LINE_ITEM_TYPE_VIDEO_DEFAULT"
    videoMobileAppInstall = "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INSTALL"
    displayMobileAppInventory = "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INVENTORY"
    videoMobileAppInventory = "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INVENTORY"
    audioDefault = "LINE_ITEM_TYPE_AUDIO_DEFAULT"
    videoOverTheTop = "LINE_ITEM_TYPE_VIDEO_OVER_THE_TOP"
    youtubeAndPartnersAction = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_ACTION"
    youtubeAndPartnersNonSkippable = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_NON_SKIPPABLE"
    youtubeAndPartnersVideoSequence = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIDEO_SEQUENCE"
    youtubeAndPartnersAudio = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_AUDIO"
    youtubeAndPartnersReach = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_REACH"
    youtubeAndPartnersSimple = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_SIMPLE"
    youtubeAndPartnersNonSkippableOverTheTop = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_NON_SKIPPABLE_OVER_THE_TOP"
    youtubeAndPartnersReachOverTheTop = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_REACH_OVER_THE_TOP"
    youtubeAndPartnersSimpleOverTheTop = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_SIMPLE_OVER_THE_TOP"
    youtubeAndPartnersTargetFrequency = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_TARGET_FREQUENCY"
    youtubeAndPartnersTargetView = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIEW"


class TrackingFloodlightActivityConfig(BaseModel):
    floodlightActivityId: str
    postClickLookbackWindowDays: int
    postViewLookbackWindowDays: int


class ConversionCountingConfig(BaseModel):
    postViewCountPercentageMillis: Optional[str] = None
    floodlightActivityConfigs: Optional[List[TrackingFloodlightActivityConfig]] = None


class LineItem(BaseModel):
    name: str
    advertiserId: str
    campaignId: str
    insertionOrderId: str
    lineItemId: str
    displayName: str
    lineItemType: LineItemType
    entityStatus: dv3.EntityStatus
    updateTime: str
    partnerCosts: List[dv3.PartnerCost] = []
    flight: LineItemFlight
    budget: LineItemBudget
    pacing: dv3.Pacing
    frequencyCap: dv3.FrequencyCap
    partnerRevenueModel: dv3.PartnerRevenueModel
    conversionCounting: Optional[ConversionCountingConfig] = None
    creativeIds: List[str] = []
    bidStrategy: dv3.BiddingStrategy
    integrationDetails: dv3.IntegrationDetails
    targetingExpansion: Optional[TargetingExpansionConfig] = None
    warningMessages: List[LineItemWarningMessage] = []
    mobileApp: MobileApp = None
