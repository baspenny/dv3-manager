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
    unspecified = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_UNSPECIFIED"
    manualCPV = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPV"
    manualCPM = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPM"
    targetCPA = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPA"
    maxCPM = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPMA"
    maxLift = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_LIFT"
    maxConversions = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSIONS"
    targetCPV = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPVA"
    targetROAS = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_ROASA"
    maxConversionValue = "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSION_VALUE"


class BiddingSource(str, Enum):
    """Mogelijke bronnen voor de effectieve doel-CPA van de advertentiegroep."""
    unspecified = "BIDDING_SOURCE_UNSPECIFIED"  # Bidding source is not specified or unknown
    lineItem = "BIDDING_SOURCE_LINE_ITEM"  # Bidding value is inherited from the line item
    adGroup = "BIDDING_SOURCE_AD_GROUP"  # Bidding value is defined in the ad group


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


class Exchange(str, Enum):
    unspecified = 'EXCHANGE_UNSPECIFIED'
    googleAdManager = 'EXCHANGE_GOOGLE_AD_MANAGER'
    appNexus = 'EXCHANGE_APPNEXUS'
    brightroll = 'EXCHANGE_BRIGHTROLL'
    adform = 'EXCHANGE_ADFORM'
    admeta = 'EXCHANGE_ADMETA'
    admixer = 'EXCHANGE_ADMIXER'
    adsmogo = 'EXCHANGE_ADSMOGO'
    adswizz = 'EXCHANGE_ADSWIZZ'
    bidswitch = 'EXCHANGE_BIDSWITCH'
    brightrollDisplay = 'EXCHANGE_BRIGHTROLL_DISPLAY'
    cadreon = 'EXCHANGE_CADREON'
    dailymotion = 'EXCHANGE_DAILYMOTION'
    five = 'EXCHANGE_FIVE'
    fluct = 'EXCHANGE_FLUCT'
    freewheel = 'EXCHANGE_FREEWHEEL'
    geniee = 'EXCHANGE_GENIEE'
    gumgum = 'EXCHANGE_GUMGUM'
    imobile = 'EXCHANGE_IMOBILE'
    ibillboard = 'EXCHANGE_IBILLBOARD'
    improveDigital = 'EXCHANGE_IMPROVE_DIGITAL'
    index = 'EXCHANGE_INDEX'
    kargo = 'EXCHANGE_KARGO'
    microad = 'EXCHANGE_MICROAD'
    mopub = 'EXCHANGE_MOPUB'
    nend = 'EXCHANGE_NEND'
    oneByAolDisplay = 'EXCHANGE_ONE_BY_AOL_DISPLAY'
    oneByAolMobile = 'EXCHANGE_ONE_BY_AOL_MOBILE'
    oneByAolVideo = 'EXCHANGE_ONE_BY_AOL_VIDEO'
    ooyala = 'EXCHANGE_OOYALA'
    openx = 'EXCHANGE_OPENX'
    permodo = 'EXCHANGE_PERMODO'
    platformOne = 'EXCHANGE_PLATFORMONE'
    platformId = 'EXCHANGE_PLATFORMID'
    pubmatic = 'EXCHANGE_PUBMATIC'
    pulsepoint = 'EXCHANGE_PULSEPOINT'
    revenueMax = 'EXCHANGE_REVENUEMAX'
    rubicon = 'EXCHANGE_RUBICON'
    smartclip = 'EXCHANGE_SMARTCLIP'
    smartrtb = 'EXCHANGE_SMARTRTB'
    smartstreamTv = 'EXCHANGE_SMARTSTREAMTV'
    sovrn = 'EXCHANGE_SOVRN'
    spotxchange = 'EXCHANGE_SPOTXCHANGE'
    stroer = 'EXCHANGE_STROER'
    teadstv = 'EXCHANGE_TEADSTV'
    telaria = 'EXCHANGE_TELARIA'
    tvn = 'EXCHANGE_TVN'
    united = 'EXCHANGE_UNITED'
    yieldlab = 'EXCHANGE_YIELDLAB'
    yieldmo = 'EXCHANGE_YIELDMO'
    unrulyx = 'EXCHANGE_UNRULYX'
    open8 = 'EXCHANGE_OPEN8'
    triton = 'EXCHANGE_TRITON'
    triplelift = 'EXCHANGE_TRIPLELIFT'
    taboola = 'EXCHANGE_TABOOLA'
    inmobi = 'EXCHANGE_INMOBI'
    smaato = 'EXCHANGE_SMAATO'
    aja = 'EXCHANGE_AJA'
    supership = 'EXCHANGE_SUPERSHIP'
    nexstarDigital = 'EXCHANGE_NEXSTAR_DIGITAL'
    waze = 'EXCHANGE_WAZE'
    soundcast = 'EXCHANGE_SOUNDCAST'
    sharethrough = 'EXCHANGE_SHARETHROUGH'
    fyber = 'EXCHANGE_FYBER'
    redForPublishers = 'EXCHANGE_RED_FOR_PUBLISHERS'
    medianet = 'EXCHANGE_MEDIANET'
    tapjoy = 'EXCHANGE_TAPJOY'
    vistar = 'EXCHANGE_VISTAR'
    dax = 'EXCHANGE_DAX'
    jcd = 'EXCHANGE_JCD'
    placeExchange = 'EXCHANGE_PLACE_EXCHANGE'
    applovin = 'EXCHANGE_APPLOVIN'
    connatix = 'EXCHANGE_CONNATIX'
    resetDigital = 'EXCHANGE_RESET_DIGITAL'
    hivestack = 'EXCHANGE_HIVESTACK'
    applovinGbid = 'EXCHANGE_APPLOVIN_GBID'
    fyberGbid = 'EXCHANGE_FYBER_GBID'
    unityGbid = 'EXCHANGE_UNITY_GBID'
    chartboostGbid = 'EXCHANGE_CHARTBOOST_GBID'
    admostGbid = 'EXCHANGE_ADMOST_GBID'
    toponGbid = 'EXCHANGE_TOPON_GBID'


class SdfVersion(str, Enum):
    V5 = "SDF_VERSION_5"
    V5_4 = "SDF_VERSION_5_4"
    V5_5 = "SDF_VERSION_5_5"
    V6 = "SDF_VERSION_6"
    V7 = "SDF_VERSION_7"

class SdfConfig(BaseModel):
    version: SdfVersion
    adminEmail: Optional[str] = None