import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Order, Product

stripe.api_key = settings.STRIPE_SECRET_KEY

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
    # stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        success_url=domain + 'success',
        cancel_url=domain + 'cancel',
        mode='payment',
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


class OrderList(ListView):
    model = Order


class OrderDetail(DetailView):
    model = Order
    extra_context = {
        'publicKey': settings.STRIPE_PUBLISHABLE_KEY
    }


def order_buy(request, pk):
    domain = settings.ACTIVE_DOMAIN
    order = Order.objects.get(id=pk)
    # stripe.api_key = settings.STRIPE_SECRET_KEY
    discount = order.discount.id_coupon
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        success_url=domain + 'success',
        cancel_url=domain + 'cancel',
        mode='payment',
        discounts=[{
              'coupon': discount
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
        'quantity': 1} for product in order.product.all()
        ]
    )
    return JsonResponse({'sessionId': checkout_session['id']})
