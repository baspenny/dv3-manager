import unittest
import os


class TestService(unittest.TestCase):
    def test_service(self):
        from dv3.service import build_service

        print('TestService: Creating service')
        service = build_service(os.environ.get("SA_PRINCIPAL"))

        print('TestService: Listing partners, fetching first page of results')
        res = service.partners().list().execute()


        print(len(res.get('partners', [])))

        self.assertTrue(True)