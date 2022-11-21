from django.shortcuts import render
from .models import Product
from django.conf import settings
from django.http.response import JsonResponse
import stripe


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


def buy(request, id):
    domain = settings.ACTIVE_DOMAIN
    product = Product.objects.get(id=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # coupon = stripe.Coupon.create(percent_off=20, duration="once")
    # print(coupon)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        success_url=domain + 'success',
        cancel_url=domain + 'cancel',
        mode='payment',
        discounts=[{
            # 'coupon': coupon.id
            'coupon': 'E2UnkIyG'
        }],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': product.price,
                'product_data': {
                    'name': product.name,
                    'description': product.description
                }
            },
            'quantity': 1
        },
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': 333,
                    'product_data': {
                        'name': 'test_product',
                        'description': 'null'
                    }
                },
                'quantity': 2
            }
        ]
    )
    return JsonResponse({'sessionId': checkout_session['id']})
