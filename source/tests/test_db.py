from unittest import TestCase

from source.db import fetch_locations


class DBTestCase(TestCase):
    def test_fetch_locations(self):
        locations = fetch_locations()
        self.assertTrue(isinstance(locations, dict))
        self.assertTrue(len(locations) > 1)
