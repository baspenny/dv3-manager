from typing import List, Optional

from pydantic import BaseModel
import dv3


class EnabledExchange(BaseModel):
    exchange: Optional[dv3.Exchange] = None
    googleAdManagerAgencyId: Optional[str] = None
    googleAdManagerBuyerNetworkId: Optional[str] = None
    seatId: Optional[str] = None


class ExchangeConfig(BaseModel):
    enabledExchanges: Optional[List[EnabledExchange]] = None


class PartnerGeneralConfig(BaseModel):
    timeZone: str
    currencyCode: str


class MeasurementConfig(BaseModel):
    dv360ToCmCostReportingEnabled: Optional[bool] = None
    dv360ToCmDataSharingEnabled: Optional[bool] = None


class PartnerAdServerConfig(BaseModel):
    measurementConfig: MeasurementConfig


class PartnerDataAccessConfig(BaseModel):
    sdfConfig: dv3.SdfConfig


class PartnerBillingConfig(BaseModel):
    billingProfileId: str


class Partner(BaseModel):
    name: str
    partnerId: str
    updateTime: str
    displayName: str
    entityStatus: dv3.EntityStatus
    generalConfig: PartnerGeneralConfig
    adServerConfig: PartnerAdServerConfig
    dataAccessConfig: PartnerDataAccessConfig
    exchangeConfig: ExchangeConfig
    billingConfig: PartnerBillingConfig
