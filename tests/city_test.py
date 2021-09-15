import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city1 = City("Barcelona", "Spain")
        self.city2 = City("Prague", "Czech Republic")

    def test_city_has_country(self):
        self.assertEqual("Spain", self.city1.country)

    def test_city_has_name(self):
        self.assertEqual("Prague", self.city2.name)