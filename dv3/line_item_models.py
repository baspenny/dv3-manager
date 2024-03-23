from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

from dv3.enums import EntityStatus, DateRange


class PartnerCostType(str, Enum):
    unspecified = "PARTNER_COST_TYPE_UNSPECIFIED"
    adloox = "PARTNER_COST_TYPE_ADLOOX"
    adloox_prebid = "PARTNER_COST_TYPE_ADLOOX_PREBID"
    adsafe = "PARTNER_COST_TYPE_ADSAFE"
    adxpose = "PARTNER_COST_TYPE_ADXPOSE"
    aggregate_knowledge = "PARTNER_COST_TYPE_AGGREGATE_KNOWLEDGE"
    agency_trading_desk = "PARTNER_COST_TYPE_AGENCY_TRADING_DESK"
    dv360_fee = "PARTNER_COST_TYPE_DV360_FEE"
    comscore_vce = "PARTNER_COST_TYPE_COMSCORE_VCE"
    data_management_platform = "PARTNER_COST_TYPE_DATA_MANAGEMENT_PLATFORM"
    default = "PARTNER_COST_TYPE_DEFAULT"
    double_verify = "PARTNER_COST_TYPE_DOUBLE_VERIFY"
    double_verify_prebid = "PARTNER_COST_TYPE_DOUBLE_VERIFY_PREBID"
    evidon = "PARTNER_COST_TYPE_EVIDON"
    integral_ad_science_video = "PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE_VIDEO"
    integral_ad_science_prebid = "PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE_PREBID"
    media_cost_data = "PARTNER_COST_TYPE_MEDIA_COST_DATA"
    moat_video = "PARTNER_COST_TYPE_MOAT_VIDEO"
    nielsen_dar = "PARTNER_COST_TYPE_NIELSEN_DAR"
    shop_local = "PARTNER_COST_TYPE_SHOP_LOCAL"
    teracent = "PARTNER_COST_TYPE_TERACENT"
    third_party_ad_server = "PARTNER_COST_TYPE_THIRD_PARTY_AD_SERVER"
    trust_metrics = "PARTNER_COST_TYPE_TRUST_METRICS"
    vizu = "PARTNER_COST_TYPE_VIZU"
    adlingo_fee = "PARTNER_COST_TYPE_ADLINGO_FEE"
    custom_fee_1 = "PARTNER_COST_TYPE_CUSTOM_FEE_1"
    custom_fee_2 = "PARTNER_COST_TYPE_CUSTOM_FEE_2"
    custom_fee_3 = "PARTNER_COST_TYPE_CUSTOM_FEE_3"
    custom_fee_4 = "PARTNER_COST_TYPE_CUSTOM_FEE_4"
    custom_fee_5 = "PARTNER_COST_TYPE_CUSTOM_FEE_5"
    scibids_fee = "PARTNER_COST_TYPE_SCIBIDS_FEE"


class PartnerCostFeeType(str, Enum):
    unspecified = "PARTNER_COST_FEE_TYPE_UNSPECIFIED"
    cpm_fee = "PARTNER_COST_FEE_TYPE_CPM_FEE"
    media_fee = "PARTNER_COST_FEE_TYPE_MEDIA_FEE"


class PartnerCostInvoiceType(str, Enum):
    unspecified = "PARTNER_COST_INVOICE_TYPE_UNSPECIFIED"
    dv360 = "PARTNER_COST_INVOICE_TYPE_DV360"
    partner = "PARTNER_COST_INVOICE_TYPE_PARTNER"


class PartnerCost(BaseModel):
    costType: PartnerCostType
    feeType: PartnerCostFeeType
    invoiceType: PartnerCostInvoiceType
    feeAmount: Optional[str] = None
    feePercentageMillis: Optional[str] = None


class LineItemFlightDateType(str, Enum):
    unspecified = "LINE_ITEM_FLIGHT_DATE_TYPE_UNSPECIFIED"
    inherited = "LINE_ITEM_FLIGHT_DATE_TYPE_INHERITED"
    custom = "LINE_ITEM_FLIGHT_DATE_TYPE_CUSTOM"


class LineItemFlight(BaseModel):
    flightDateType: LineItemFlightDateType
    dateRange: DateRange


class BudgetUnit(str, Enum):
    unspecified = "BUDGET_UNIT_UNSPECIFIED"
    currency = "BUDGET_UNIT_CURRENCY"
    impressions = "BUDGET_UNIT_IMPRESSIONS"


class LineItemBudgetAllocationType(str, Enum):
    unspecified = "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNSPECIFIED"
    automatic = "LINE_ITEM_BUDGET_ALLOCATION_TYPE_AUTOMATIC"
    fixed = "LINE_ITEM_BUDGET_ALLOCATION_TYPE_FIXED"
    unlimited = "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNLIMITED"


class LineItemBudget(BaseModel):
    budgetAllocationType: Optional[LineItemBudgetAllocationType] = None
    budgetUnit: Optional[BudgetUnit] = None
    maxAmount: str = ''


class PacingPeriod(str, Enum):
    unspecified = "PACING_PERIOD_UNSPECIFIED"
    daily = "PACING_PERIOD_DAILY"
    flight = "PACING_PERIOD_FLIGHT"


class PacingType(str, Enum):
    unspecified = "PACING_TYPE_UNSPECIFIED"
    ahead = "PACING_TYPE_AHEAD"
    asap = "PACING_TYPE_ASAP"
    even = "PACING_TYPE_EVEN"


class Pacing(BaseModel):
    pacingPeriod: PacingPeriod
    pacingType: PacingType
    dailyMaxMicros: str = None
    dailyMaxImpressions: str = None


class TimeUnit(str, Enum):
    unspecified = "TIME_UNIT_UNSPECIFIED"
    lifetime = "TIME_UNIT_LIFETIME"
    months = "TIME_UNIT_MONTHS"
    weeks = "TIME_UNIT_WEEKS"
    days = "TIME_UNIT_DAYS"
    hours = "TIME_UNIT_HOURS"
    minutes = "TIME_UNIT_MINUTES"


class FrequencyCap(BaseModel):
    unlimited: bool = None
    timeUnit: TimeUnit = None
    timeUnitCount: int = None
    maxImpressions: int = None
    maxViews: int = None


class PartnerRevenueModelMarkupType(Enum):
    unspecified = "PARTNER_REVENUE_MODEL_MARKUP_TYPE_UNSPECIFIED"
    cpm = "PARTNER_REVENUE_MODEL_MARKUP_TYPE_CPM"
    mediaCostMarkup = "PARTNER_REVENUE_MODEL_MARKUP_TYPE_MEDIA_COST_MARKUP"
    totalMediaCostMarkup = "PARTNER_REVENUE_MODEL_MARKUP_TYPE_TOTAL_MEDIA_COST_MARKUP"


class PartnerRevenueModel(BaseModel):
    markup_type: Optional[PartnerRevenueModelMarkupType] = None
    markup_amount: Optional[str] = None


class ConversionCountingConfig(BaseModel):
    # Define fields for ConversionCountingConfig if needed
    pass


class BiddingStrategy(BaseModel):
    # Define fields for BiddingStrategy if needed
    pass


class IntegrationDetails(BaseModel):
    # Define fields for IntegrationDetails if needed
    pass


class AudienceExpansionLevel(str, Enum):
    unspecified = "AUDIENCE_EXPANSION_LEVEL_UNSPECIFIED"
    none = "NONE"
    minimal = "MINIMAL"
    agressive = "AGRESSIVE"


class TargetingExpansionConfig(BaseModel):
    enableOptimizedTargeting: Optional[bool] = None
    audienceExpansionSeedListExcluded: Optional[bool] = None
    audienceExpansionLevel: Optional[AudienceExpansionLevel] = None


class MobileApp(BaseModel):
    # Define fields for MobileApp if needed
    pass


class LineItemWarningMessage(str, Enum):
    unspecified = "LINE_ITEM_WARNING_MESSAGE_UNSPECIFIED"
    invalid_flight_dates = "INVALID_FLIGHT_DATES"
    expired = "EXPIRED"
    pending_flight = "PENDING_FLIGHT"
    all_partner_enabled_exchanges_negatively_targeted = "ALL_PARTNER_ENABLED_EXCHANGES_NEGATIVELY_TARGETED"
    invalid_inventory_source = "INVALID_INVENTORY_SOURCE"
    app_inventory_invalid_site_targeting = "APP_INVENTORY_INVALID_SITE_TARGETING"
    app_inventory_invalid_audience_lists = "APP_INVENTORY_INVALID_AUDIENCE_LISTS"
    no_valid_creative = "NO_VALID_CREATIVE"
    parent_insertion_order_paused = "PARENT_INSERTION_ORDER_PAUSED"
    parent_insertion_order_expired = "PARENT_INSERTION_ORDER_EXPIRED"


class LineItemType(str, Enum):
    # Line item types DV360 API v1 and v2
    unspecified = "LINE_ITEM_TYPE_UNSPECIFIED"
    display_default = "LINE_ITEM_TYPE_DISPLAY_DEFAULT"
    display_mobile_app_install = "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INSTALL"
    video_default = "LINE_ITEM_TYPE_VIDEO_DEFAULT"
    video_mobile_app_install = "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INSTALL"
    display_mobile_app_inventory = "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INVENTORY"
    video_mobile_app_inventory = "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INVENTORY"
    audio_default = "LINE_ITEM_TYPE_AUDIO_DEFAULT"
    video_over_the_top = "LINE_ITEM_TYPE_VIDEO_OVER_THE_TOP"
    # Line item types DV360 API v2
    youtube_and_partners_action = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_ACTION"
    youtube_and_partners_non_skippable = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_NON_SKIPPABLE"
    youtube_and_partners_video_sequence = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIDEO_SEQUENCE"
    youtube_and_partners_audio = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_AUDIO"
    youtube_and_partners_reach = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_REACH"
    youtube_and_partners_simple = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_SIMPLE"
    youtube_and_partners_non_skippable_over_the_top = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_NON_SKIPPABLE_OVER_THE_TOP"
    youtube_and_partners_reach_over_the_top = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_REACH_OVER_THE_TOP"
    youtube_and_partners_simple_over_the_top = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_SIMPLE_OVER_THE_TOP"
    youtube_and_partners_target_frequency = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_TARGET_FREQUENCY"
    youtube_and_partners_target_view = "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIEW"


class LineItem(BaseModel):
    name: str
    advertiserId: str
    campaignId: str
    insertionOrderId: str
    lineItemId: str
    displayName: str
    lineItemType: LineItemType
    entityStatus: EntityStatus
    updateTime: str
    partnerCosts: List[PartnerCost] = []
    flight: LineItemFlight
    budget: LineItemBudget
    pacing: Pacing
    frequencyCap: FrequencyCap
    partnerRevenueModel: PartnerRevenueModel
    conversionCounting: ConversionCountingConfig
    creativeIds: List[str] = []
    bidStrategy: BiddingStrategy
    integrationDetails: IntegrationDetails
    targetingExpansion: Optional[TargetingExpansionConfig] = None
    warningMessages: List[LineItemWarningMessage] = []
    mobileApp: MobileApp = None
