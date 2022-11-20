from django.shortcuts import render
from .models import Product

def hello(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'purchases/index.html', context=context)
