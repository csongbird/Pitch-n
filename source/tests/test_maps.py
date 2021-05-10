from unittest import TestCase
from source.maps import generate_map
from folium import Map
import os

class TestMaps(TestCase):
    def test_generate_map(self):
        os.chdir('..')
        map = generate_map()
        self.assertEqual(map, 200)