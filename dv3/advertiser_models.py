from pydantic import BaseModel
from typing import Optional
import dv3


class AdvertiserGeneralConfig(BaseModel):
    domainUrl: str
    timeZone: Optional[str] = None
    currencyCode: str


class CmHybridConfig(BaseModel):
    cmAccountId: Optional[str] = None
    cmFloodlightConfigId: str
    cmAdvertiserIds: Optional[list[str]] = None
    cmSyncableSiteIds: Optional[list[str]] = None
    dv360ToCmDataSharingEnabled: Optional[bool] = None
    dv360ToCmCostReportingEnabled: Optional[bool] = None
    cmFloodlightLinkingAuthorized: bool


class ThirdPartyOnlyConfig(BaseModel):
    pixelOrderIdReportingEnabled: Optional[bool] = None


class AdvertiserAdServerConfig(BaseModel):
    cmHybridConfig: Optional[CmHybridConfig] = None
    thirdPartyOnlyConfig: Optional[ThirdPartyOnlyConfig] = None


class AdvertiserCreativeConfig(BaseModel):
    iasClientId: Optional[str] = None
    obaComplianceDisabled: Optional[bool] = None
    dynamicCreativeEnabled: Optional[bool] = None
    videoCreativeDataSharingAuthorized: Optional[bool] = None


class AdvertiserSdfConfig(BaseModel):
    overridePartnerSdfConfig: Optional[bool] = None
    sdfConfig: dv3.SdfConfig = None


class AdvertiserDataAccessConfig(BaseModel):
    sdfConfig: Optional[AdvertiserSdfConfig] = None


class IntegrationDetails(BaseModel):
    integrationCode: Optional[str] = None
    details: Optional[str] = None


class AdvertiserTargetingConfig(BaseModel):
    exemptTvFromViewabilityTargeting: Optional[bool] = None


class AdvertiserBillingConfig(BaseModel):
    billingProfileId: Optional[str] = None


class Advertiser(BaseModel):
    name: str
    advertiserId: str
    partnerId: str
    displayName: str
    entityStatus: dv3.EntityStatus
    updateTime: str
    generalConfig: AdvertiserGeneralConfig
    adServerConfig: AdvertiserAdServerConfig
    creativeConfig: AdvertiserCreativeConfig
    dataAccessConfig: Optional[AdvertiserDataAccessConfig] = None
    integrationDetails: Optional[IntegrationDetails] = None
    servingConfig: Optional[AdvertiserTargetingConfig] = None
    prismaEnabled: Optional[bool] = None
    billingConfig: Optional[AdvertiserBillingConfig] = None
