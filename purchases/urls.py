from django.urls import path
from .views import hello, items, buy


urlpatterns = [
    path('', hello),
    path('item/<int:id>/', items),
    path('buy/<int:id>/', buy),
]