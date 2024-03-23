# from typing import Optional
# from dv3.enums import EntityStatus
#
# from pydantic import BaseModel
#
#
#
#
#
# class CampaignGoal(BaseModel):
#     campaignGoalType: Optional[str] = None
#     performanceGoal: Optional[str] = None
#
#
# class Campaign(BaseModel):
#     name: Optional[str] = None
#     advertiserId: Optional[str] = None
#     campaignId: Optional[str] = None
#     displayName: Optional[str] = None
#     entityStatus: Optional[EntityStatus] = None
#     updateTime: Optional[str] = None
#
#     campaignGoal: Optional[str] = None
#     campaignFlight: Optional[str] = None
#     frequencyCap: Optional[str] = None
#     campaignBudgets: Optional[str] = None