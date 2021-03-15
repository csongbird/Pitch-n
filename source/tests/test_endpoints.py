from unittest import TestCase
from flask_restx import Resource

from source.endpoints import Home, Endpoints, Locations
from source.endpoints import SUCCESS, AVAILABLE


class TestEndpoints(TestCase):
    def test_home(self):
        ret = Home(Resource).get()
        self.assertIn(SUCCESS, ret)


    def test_endpoints(self):
        ret = Endpoints(Resource).get()
        self.assertIn(AVAILABLE, ret)


    def test_Locations(self):
        locations = Locations(Resource).get()
        self.assertIsInstance(locations, dict)
        self.assertGreater(len(locations), 1)
