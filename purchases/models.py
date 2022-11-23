import stripe
from django.conf import settings
from django.db import models

stripe.api_key = settings.STRIPE_SECRET_KEY

def valid(data):
    if data < 50:
        raise Exception('value must be more then 50 centes')

class Product(models.Model):
    name = models.CharField('Name', max_length=256)
    description = models.CharField('Description', max_length=256, null=True, blank=True)
    price = models.IntegerField('Price', validators=[valid])

    def __str__(self):
        return self.name

class Discount(models.Model):
    id_coupon = models.CharField(max_length=256, null=True, blank=True)
    percent_off = models.CharField(max_length=256)
    name = models.CharField('Name', max_length=256, null=True, blank=True)
    choices = [
        ('once', 'once'),
        ('repeating', 'repeating'),
        ('forever', 'forever')]
    duration = models.CharField(choices=choices, max_length=256)


    def __str__(self):
        return (self.name if not self.name is None else 'None') + ' ' + str(self.percent_off)


class Order(models.Model):
    product = models.ManyToManyField(Product)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return ', '.join([i.name for i in self.product.all()])
