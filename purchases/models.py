from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=256)
    description = models.CharField('Description', max_length=256, null=True, blank=True)
    price = models.IntegerField('Price')
    def __str__(self):
        return self.name
