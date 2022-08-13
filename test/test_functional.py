
import unittest
from metals.metal_prices import fetch_data, fetch_stats
from vcr_unittest import VCRTestCase

class MyTest(VCRTestCase):

	def test_Silver_fetch_data(self):
		status, values = fetch_data('Silver')
		self.assertEqual(first=200, second=status)
		self.assertEqual(len(self.cassette), 1)
		self.assertEqual(self.cassette.requests[0].uri, "https://www.goldapi.io/api/XAG/USD")
		print(self.cassette.requests[0].uri)

	def test_fetch_stats(self):
		status, values = fetch_stats()
		self.assertEqual(first=200, second=status)

if __name__ == '__main__':
	unittest.main()
