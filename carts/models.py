from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Cart(models.Model):
    cart_user_id = models.IntegerField(validators=[MinValueValidator(0)])
    cart_total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])


class Order(models.Model):
    order_user_id = models.IntegerField(validators=[MinValueValidator(0)])
    order_order_id = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
