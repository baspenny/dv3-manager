from pydantic import BaseModel
from enum import Enum
from typing import Optional


class PartnerCostFeeType(str, Enum):
    unspecified = "PARTNER_COST_FEE_TYPE_UNSPECIFIED"
    cpm_fee = "PARTNER_COST_FEE_TYPE_CPM_FEE"
    media_fee = "PARTNER_COST_FEE_TYPE_MEDIA_FEE"


class PartnerCostInvoiceType(str, Enum):
    unspecified = "PARTNER_COST_INVOICE_TYPE_UNSPECIFIED"
    dv360 = "PARTNER_COST_INVOICE_TYPE_DV360"
    partner = "PARTNER_COST_INVOICE_TYPE_PARTNER"


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


class PartnerCost(BaseModel):
    costType: PartnerCostType
    feeType: PartnerCostFeeType
    invoiceType: PartnerCostInvoiceType
    feeAmount: Optional[str] = None
    feePercentageMillis: Optional[str] = None


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


class FixedBidStrategy(BaseModel):
    bidAmountMicros: Optional[str] = None


class BiddingStrategyPerformanceGoalType(str, Enum):
    unspecified = "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED"
    cpa = "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPA"
    cpc = "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPC"
    viewableCpm = "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM"
    customAlgo = "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO"
    civa = "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CIVA"
    ivoTen = "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_IVO_TEN"
    avViewed = "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_AV_VIEWED"


class MaximizeSpendBidStrategy(BaseModel):
    performanceGoalType: Optional[BiddingStrategyPerformanceGoalType] = None
    maxAverageCpmBidAmountMicros: Optional[str] = None
    raiseBidForDeals: Optional[bool] = None
    customBiddingAlgorithmId: Optional[str] = None


class PerformanceGoalBidStrategy(BaseModel):
    performanceGoalType: Optional[BiddingStrategyPerformanceGoalType] = None
    performanceGoalAmountMicros: Optional[str] = None
    maxAverageCpmBidAmountMicros: Optional[str] = None
    customBiddingAlgorithmId: Optional[str] = None


class YoutubeAndPartnersBiddingStrategyType(str, Enum):
    UNSPECIFIED = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_UNSPECIFIED"
    MANUAL_CPV = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPV"
    MANUAL_CPM = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPM"
    TARGET_CPA = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPA"
    MAX_CPM = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPMA"
    MAX_LIFT = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_LIFT"
    MAX_CONVERSIONS = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSIONS"
    TARGET_CPV = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPVA"
    TARGET_ROAS = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_ROASA"
    MAX_CONVERSION_VALUE = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSION_VALUE"


class BiddingSource(str, Enum):
    """Mogelijke bronnen voor de effectieve doel-CPA van de advertentiegroep."""
    UNSPECIFIED = "BIDDING_SOURCE_UNSPECIFIED"  # Bidding source is not specified or unknown
    LINE_ITEM = "BIDDING_SOURCE_LINE_ITEM"  # Bidding value is inherited from the line item
    AD_GROUP = "BIDDING_SOURCE_AD_GROUP"  # Bidding value is defined in the ad group


class YoutubeAndPartnersBiddingStrategy(BaseModel):
    type: Optional[YoutubeAndPartnersBiddingStrategyType] = None
    value: Optional[str] = None
    adGroupEffectiveTargetCpaValue: Optional[str] = None
    adGroupEffectiveTargetCpaSource: Optional[BiddingSource] = None


class BiddingStrategy(BaseModel):
    fixedBidStrategy: Optional[FixedBidStrategy] = None
    maximizeSpendBidStrategy: Optional[MaximizeSpendBidStrategy] = None
    performanceGoalBidStrategy: Optional[PerformanceGoalBidStrategy] = None
    youtubeAndPartnersBiddingStrategy: Optional[YoutubeAndPartnersBiddingStrategy] = None


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

class BudgetUnit(str, Enum):
    unspecified = "BUDGET_UNIT_UNSPECIFIED"
    currency = "BUDGET_UNIT_CURRENCY"
    impressions = "BUDGET_UNIT_IMPRESSIONS"
