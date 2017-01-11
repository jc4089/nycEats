"""
tests.py
"""

from django.test import TestCase
from .models import Restaurant

class RestaurantMethodTests(TestCase):
    def test_is_thai(self):
        """
        is_thai() should return True if the restaurant is Thai, False otherwise
        """
        
        thai_restaurant = Restaurant(
            camis = 1,
            name = 'Thai Jasmine Restaurant',
            boro = 'Manhattan',
            building = '106',
            street = 'Bayard',
            zipcode = 10013,
            phone = 2123493132,
            cuisine = 'Thai',
        )
        
        self.assertIs(thai_restaurant.is_thai(), True)
        
        chinese_restaurant = Restaurant(
            camis = 2,
            name = 'Mission Chinese Food',
            boro = 'Manhattan',
            building = '171',
            street = 'East Broadway',
            zipcode = 10002,
            phone = 2125298800,
            cuisine = 'Chinese',
        )
        
        self.assertIs(chinese_restaurant.is_thai(), False)