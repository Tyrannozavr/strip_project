from django.db import models
import stripe
from django.conf import settings

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
    id_coupon = models.CharField(max_length=256)
    percent_off = models.CharField(max_length=256)
    name = models.CharField('Name', max_length=256, null=True, blank=True)

    def simple_create(percent_off, duration):
        """simple creating discount without visiting site percent_off can't be 100% and duration must be once,
        repeating or forever"""

        if duration not in ['once', 'repeating', 'forever']:
            raise Exception('duraton must be once, repeating or forever')
        stripe.api_key = settings.STRIPE_SECRET_KEY
        coupon = stripe.Coupon.create(percent_off=percent_off, duration=duration)
        Discount.objects.create(id_coupon=coupon.id, percent_off=coupon.percent_off, name=coupon.name)

    def __str__(self):
        return self.name if not self.name is None else 'None'


class Order(models.Model):
    product = models.ManyToManyField(Product)

    def __str__(self):
        return ', '.join([i.name for i in self.product.all()])
