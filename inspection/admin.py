from django.contrib import admin

from .models import Restaurant, InspectionResults

from django.contrib import admin

class InspectionInline(admin.TabularInline):
    model = InspectionResults
    extra = 3

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ID', {'fields': ['camis']}),
        ('Name', {'fields': ['name']}),
        ('Borough', {'fields': ['boro']}),
        ('Building', {'fields': ['building']}),
        ('Street', {'fields': ['street']}),
        ('Zipcode', {'fields': ['zipcode']}),
        ('Phone', {'fields': ['phone']}),
        ('Cuisine', {'fields': ['cuisine']}),
    ]
    
    # Inspection display inline
    inlines = [InspectionInline]
    
    # Display
    list_display = ('camis', 'name', 'is_thai')
    
    # search
    search_fields = ['name']

admin.site.register(Restaurant, RestaurantAdmin)