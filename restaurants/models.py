from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    category = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')

    def __str__(self):
        return self.restaurant.name
