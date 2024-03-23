import json
import unittest
from unittest.mock import Mock
from dv3.advertiser_models import Advertiser
from dv3.line_item_models import LineItem

from pathlib import Path


class TestModels(unittest.TestCase):
    # @patch('dv3.service.build_service')
    def setUp(self):
        self.service = Mock()

    def test_advertiser_model(self):
        with open(Path(__file__).parent.parent / 'test-advertiser_output.json', 'r') as f:
            mock_advertiser_data = json.load(f)
        self.service.advertisers().get().execute.return_value = mock_advertiser_data

        res = self.service.advertisers().get(
            advertiserId='3753637'
        ).execute()

        advertiser = Advertiser.model_validate(res)
        # print(advertiser.model_dump(exclude_none=True))
        self.assertEqual(advertiser.name, 'advertisers/3753637')
        self.assertEqual(advertiser.advertiserId, '3753637')
        self.assertEqual(advertiser.partnerId, '798652')

        self.assertTrue(len(advertiser.adServerConfig.cmHybridConfig.cmSyncableSiteIds) == 2)

    def test_line_item_model(self):
        with open(Path(__file__).parent.parent / 'test-line-item_output.json', 'r') as f:
            mock_line_item_data = json.load(f)
        self.service.advertisers().lineItems().get().execute.return_value = mock_line_item_data

        res = self.service.advertisers().lineItems().get(
            advertiserId='6485656018',
            lineItemId='21085527563'
        ).execute()

        line_item = LineItem.model_validate(res)

        self.assertEqual(line_item.name, 'advertisers/6485656018/lineItems/21085527563')
        self.assertTrue(len(line_item.partnerCosts) == 4)
