from django.urls import path
from .views import hello, items, buy, OrderList, OrderDetail, order_buy


urlpatterns = [
    path('', hello),
    path('item/<int:id>/', items),
    path('buy/<int:id>/', buy),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('orders/<int:pk>/buy/', order_buy),
]