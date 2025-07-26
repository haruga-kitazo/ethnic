from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=1)  # デフォルト値を設定

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PriceRange(models.Model):
    min_price = models.IntegerField()
    max_price = models.IntegerField()

    def __str__(self):
        return f"{self.min_price} - {self.max_price}"

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    nearest_station = models.CharField(max_length=255)
    walking_minutes = models.IntegerField()
    price_range = models.ForeignKey(PriceRange, on_delete=models.CASCADE)
    google_map_url = models.TextField()
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    PHOTO_TYPES = [
        ('interior', 'Interior'),
        ('exterior', 'Exterior'),
        ('food', 'Food'),
    ]
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    url = models.TextField()
    type = models.CharField(max_length=50, choices=PHOTO_TYPES)

    def __str__(self):
        return f"{self.type} - {self.restaurant.name}"

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.restaurant.name}"

class RestaurantRating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_authentic = models.BooleanField(default=False)
    is_friendly = models.BooleanField(default=False)
    has_alcohol = models.BooleanField(default=False)
    is_clean = models.BooleanField(default=False)
    is_accessible = models.BooleanField(default=False)
    is_for_girls = models.BooleanField(default=False)
    is_for_family = models.BooleanField(default=False)
    is_luxurious = models.BooleanField(default=False)
    is_unique_food = models.BooleanField(default=False)

    def __str__(self):
        return f"Ratings for {self.restaurant.name}"