from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Restaurant(models.Model):
    # Restaurant information
    camis    = models.IntegerField(unique = True, default = 1)           # Restaurant ID
    name     = models.CharField(max_length = 50, default = 'Restaurant') # Restaurant name
    boro     = models.CharField(max_length = 20, default = 'Manhattan')  # Borough
    building = models.CharField(max_length = 10, default = '0')          # Building number (can contain hypen)
    street   = models.CharField(max_length = 20, default = 'Main St')    # Street name
    zipcode  = models.IntegerField(default = 0)                          # Zip code
    phone    = models.BigIntegerField(default = 0)                       # Phone number
    cuisine  = models.CharField(max_length = 100, default = 'American')  # Cuisine description

    def __str__(self):
        return self.name
    
    def is_thai(self):
        return self.cuisine.lower() == 'thai'
    
    is_thai.admin_order_field = 'camis'
    is_thai.boolean = True
    is_thai.short_description = 'Is Thai food?'

@python_2_unicode_compatible
class InspectionResults(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    
    # Inspection information
    inspection_type = models.CharField(max_length = 100, default = '') # Type of inspection
    inspection_date = models.DateField(default = timezone.now)         # Inspection date
    grade           = models.CharField(max_length = 50, default = '')  # Inspection grade (A, B, etc.)
    score           = models.IntegerField(default = 0)                 # Inspection score
    grade_date      = models.DateField(default = timezone.now)         # Grade date

    def __str__(self):
        return self.inspection_type