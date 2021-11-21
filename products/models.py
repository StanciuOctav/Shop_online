from djongo import models
from django.core.validators import MinValueValidator


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=150, unique=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    product_description = models.CharField(max_length=300)
    product_expiration_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    product_in_stock = models.IntegerField(validators=[MinValueValidator(0)])
