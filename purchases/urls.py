from django.urls import path
from .views import hello, items


urlpatterns = [
    path('', hello),
    path('item/<int:id>/', items)
]