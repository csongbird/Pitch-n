from unittest import TestCase
from flask_restx import Resource

from source.endpoints import Endpoints, Locations
from source.endpoints import AVAILABLE


class TestEndpoints(TestCase):
    def test_endpoints(self):
        ret = Endpoints(Resource).get()
        self.assertIn(AVAILABLE, ret)


    def test_locations(self):
        locations = Locations(Resource).get()
        self.assertIsInstance(locations, dict)
        self.assertGreater(len(locations), 1)
