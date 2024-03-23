import json
import unittest
import os
# from dv3.advertiser_models import Advertiser
from dv3.line_item_models import LineItem


class TestService(unittest.TestCase):
    def test_service(self):
        from dv3.service import build_service

        print('TestService: Creating service')
        service = build_service(os.environ.get("SA_PRINCIPAL", 'incubeta-service@dqna-cloud.iam.gserviceaccount.com'))

        print('TestService: Listing partners, fetching first page of results')



        res = service.advertisers().lineItems().get(
            advertiserId='6485656018',
            lineItemId='21085527563'
        ).execute()

        line_item = LineItem.model_validate(res)
        print(line_item.model_dump(exclude_none=True))

        with open('line-item_output.json', 'w') as f:
            f.write(json.dumps(line_item.model_dump(exclude_none=True)))



        # res = service.partners().list().execute()
        # print(len(res.get('partners', [])))
        # res = service.advertisers().get(
        #     advertiserId='3753637'
        # ).execute()
        #
        # advertiser = Advertiser.model_validate(res)
        # print(advertiser.model_dump(exclude_none=True))
        #
        #
        # with open('test_service_output.json', 'w') as f:
        #     f.write(json.dumps(advertiser.model_dump(exclude_none=True)))



        self.assertTrue(True)