from django.db import models

def valid(data):
    if data < 50:
        raise Exception('value must be more then 50 centes')

class Product(models.Model):
    name = models.CharField('Name', max_length=256)
    description = models.CharField('Description', max_length=256, null=True, blank=True)
    price = models.IntegerField('Price', validators=[valid])

    def __str__(self):
        return self.name
