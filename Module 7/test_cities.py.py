import unittest
from city_functions import city_country

class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        """Test City, Country format."""
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        """Test City, Country - population xxx format."""
        result = city_country("Tokyo", "Japan", 13929286)
        self.assertEqual(result, "Tokyo, Japan - population 13929286")

    def test_city_country_population_language(self):
        """Test City, Country - population xxx, Language format."""
        result = city_country("Paris", "France", 2148000, "French")
        self.assertEqual(result, "Paris, France - population 2148000, French")

if __name__ == '__main__':
    unittest.main()
