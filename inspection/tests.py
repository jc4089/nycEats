"""
tests.py
"""

from django.test import TestCase
from .models import Restaurant
from django.urls import reverse

# Method tests
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

# View tests
class RestaurantViewTests(TestCase):
    def test_index_with_no_restaurants(self):
        """
        If no restaurants in database, appropriate message should be displayed
        """
        
        response = self.client.get(reverse('index'))
        
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, 'Can\'t find restaurants')
        
        self.assertQuerysetEqual(response.context['recommended_restaurants'], [])

# Display tests
class RestaurantDisplayTests(TestCase):
    def test_detail_with_restaurant(self):
        """
        The detail view should display the restaurant name
        """
        
        restaurant = Restaurant.objects.create(
            camis = 1,
            name = 'Gramercy Tavern',
            boro = 'Manhattan',
            building = '42',
            street = 'E 20th St',
            zipcode = 10003,
            phone = 2124770777,
            cuisine = 'American',
        )
        
        url = reverse('detail', args = (restaurant.id,))
        
        response = self.client.get(url)
        
        self.assertContains(response, restaurant.name)