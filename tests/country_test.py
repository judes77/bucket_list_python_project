import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country1 = Country("Spain", "Europe", "Spanish")
        self.country2 = Country("New Zealand", "Oceania", "English")

    def test_country_has_name(self):
        self.assertEqual("Spain", self.country1.name)

    def test_country_has_language(self):
        self.assertEqual("Spanish", self.country1.language)

    def test_country_has_continent(self):
        self.assertEqual("Oceania", self.country2.continent)
