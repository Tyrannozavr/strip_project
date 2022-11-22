from django.db import models
import stripe
from django.conf import settings

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
    id_coupon = models.CharField(max_length=256)
    percent_off = models.CharField(max_length=256)
    name = models.CharField('Name', max_length=256, null=True, blank=True)

    def simple_create(percent_off, duration, name=None):
        """simple creating discount without visiting site percent_off can't be 100% and duration must be once,
        repeating or forever"""

        if duration not in ['once', 'repeating', 'forever']:
            raise Exception('duraton must be once, repeating or forever')
        # stripe.api_key = settings.STRIPE_SECRET_KEY
        coupon = stripe.Coupon.create(percent_off=percent_off, duration=duration, name=name)
        Discount.objects.create(id_coupon=coupon.id, percent_off=coupon.percent_off, name=coupon.name)

    def __str__(self):
        return (self.name if not self.name is None else 'None') + ' ' + str(self.percent_off)

class Tax(models.Model):
    id_tax = models.CharField('ID', max_length=256)
    display_name = models.CharField('Name', max_length=256)
    inclusive = models.BooleanField('inclusive', default=False)
    percentage = models.DecimalField('percantage', max_digits=8, decimal_places=2)

    def simple_create(display_name, percentage, inclusive=False):
        """simple creating tax"""
        tax = stripe.TaxRate.create(
            display_name=display_name,
            inclusive=inclusive,
            percentage=percentage)
        Tax.objects.create(id_tax=tax.id, display_name=tax.display_name, inclusive=tax.inclusive, percentage=percentage)


    def __str__(self):
        return self.display_name + ' ' + str(self.percentage)

class Order(models.Model):
    product = models.ManyToManyField(Product)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return ', '.join([i.name for i in self.product.all()])
