import unittest


class AmazonMwsTestCase(unittest.TestCase):
    def test_countries(self):
        from we_pyutils.amazonmws.country import Countries
        countries = Countries()
        self.assertEqual(countries.ids[0], 'BR')
        self.assertEqual(countries.marketplace_ids[0], 'A2Q3Y263D00KWC')
        self.assertEqual(countries.marketplace_ids_kv['BR'], 'A2Q3Y263D00KWC')
        self.assertEqual(countries.mws_endpoints[0], 'mws.amazonservices.com')
        self.assertEqual(countries.mws_endpoints_kv['BR'], 'mws.amazonservices.com')


if __name__ == '__main__':
    unittest.main()
