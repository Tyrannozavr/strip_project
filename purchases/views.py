from django.shortcuts import render
from .models import Product
from django.conf import settings


def hello(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'purchases/index.html', context=context)


def items(request, id):
    product = Product.objects.get(id=id)
    context = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'publicKey': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'purchases/items.html', context=context)
