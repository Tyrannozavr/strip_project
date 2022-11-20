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
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        success_url=domain+'/success',
        cancel_url=domain+'/cancel',
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
        }]
    )
    return JsonResponse({'sessionId': checkout_session['id']})


# checkout_session = stripe.checkout.Session.create(
#     # client_reference_id=request.user.id if request.user.is_authenticated else None,
#     success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
#     cancel_url=domain_url + 'cancelled/',
#     payment_method_types=['card'],
#     mode='payment',
#     line_items=[{
#         # 'name': 'T-shirt',
#         # 'quantity': 1,
#         # 'currency': 'usd',
#         # 'amount': '2000',
#         'price_data': {
#             'currency': 'usd',
#             'unit_amount': '2000',
#             'product_data': {
#                 'name': 'T-shirt'
#             }
#         },
#         'quantity': 1
#     }
#     ]
# )
# return JsonResponse({'sessionId': checkout_session['id']})