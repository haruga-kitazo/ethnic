from django.contrib import admin
from .models import (
    Restaurant, Country, Genre, Photo, Review, RestaurantRating, PriceRange, Region
)

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Photo)
admin.site.register(Review)
admin.site.register(RestaurantRating)
admin.site.register(PriceRange)
admin.site.register(Region)