{
  "name": string,
  "advertiserId": string,
  "campaignId": string,
  "insertionOrderId": string,
  "lineItemId": string,
  "displayName": string,
  "lineItemType": enum (LineItemType),
  "entityStatus": enum (EntityStatus),
  "updateTime": string,
  "partnerCosts": [
    {
      object (PartnerCost)
    }
  ],
  "flight": {
    object (LineItemFlight)
  },
  "budget": {
    object (LineItemBudget)
  },
  "pacing": {
    object (Pacing)
  },
  "frequencyCap": {
    object (FrequencyCap)
  },
  "partnerRevenueModel": {
    object (PartnerRevenueModel)
  },
  "conversionCounting": {
    object (ConversionCountingConfig)
  },
  "creativeIds": [
    string
  ],
  "bidStrategy": {
    object (BiddingStrategy)
  },
  "integrationDetails": {
    object (IntegrationDetails)
  },
  "targetingExpansion": {
    object (TargetingExpansionConfig)
  },
  "warningMessages": [
    enum (LineItemWarningMessage)
  ],
  "mobileApp": {
    object (MobileApp)
  },
  "reservationType": enum (ReservationType),
  "excludeNewExchanges": boolean,
  "youtubeAndPartnersSettings": {
    object (YoutubeAndPartnersSettings)
  }
}