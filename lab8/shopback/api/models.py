from django.db import models
class Category(models.Model):
    name = models.CharField
    
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField
    price = models.FloatField
    description = models.TextField
    count = models.IntegerField
    is_active = models.BooleanField
    category = models.ForeignKey
    
    def __str__(self):
        return self.name
# Create your models here.
