from django.urls import path
from .views import hello, items, buy, OrderList


urlpatterns = [
    path('', hello),
    path('item/<int:id>/', items),
    path('buy/<int:id>/', buy),
    path('orders/', OrderList.as_view()),
    # path('order/<int:id>/', order_detail),
]