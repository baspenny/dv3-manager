import json
import unittest
import os
from dv3.advertiser_models import Advertiser
from dv3.line_item_models import LineItem
from dv3.partner_models import Partner
from dv3.service import build_service


class TestService(unittest.TestCase):
    def setUp(self):
        print('TestService: Creating service')
        self.service = build_service(os.environ.get(
            "SA_PRINCIPAL", 'incubeta-service@dqna-cloud.iam.gserviceaccount.com')
        )

    def test_partner(self):
        res = self.service.partners().get(
            partnerId='2104250'
        ).execute()

        advertiser = Partner.model_validate(res)
        print(advertiser.model_dump(exclude_none=True))

        with open('../test_service_output.json', 'w') as f:
            f.write(json.dumps(advertiser.model_dump(exclude_none=True)))

        self.assertTrue(True)

    def test_advertiser(self):
        res = self.service.advertisers().get(
            advertiserId='3753637'
        ).execute()

        advertiser = Advertiser.model_validate(res)
        print(advertiser.model_dump(exclude_none=True))

        with open('../test_service_output.json', 'w') as f:
            f.write(json.dumps(advertiser.model_dump(exclude_none=True)))

        self.assertTrue(True)

    def test_line_item(self):
        res = self.service.advertisers().lineItems().get(
            advertiserId='6485656018',
            lineItemId='21085527563'
        ).execute()

        line_item = LineItem.model_validate(res)
        print(line_item.model_dump(exclude_none=True))

        with open('../line-item_output.json', 'w') as f:
            f.write(json.dumps(line_item.model_dump(exclude_none=True)))
