from django.contrib import admin

from .models import Restaurant, InspectionResults

admin.site.register(Restaurant)
admin.site.register(InspectionResults)