import stripe
from django.conf import settings
from django.contrib import admin

from .models import *

stripe.api_kay = settings.STRIPE_SECRET_KEY



class DiscountAdmin(admin.ModelAdmin):
    exclude = ('id_coupon',)

    def save_model(self, request, obj, form, change):
        percent_off = request.POST.get('percent_off')
        name = request.POST.get('name')
        duration = request.POST.get('duration')
        coupon = stripe.Coupon.create(percent_off=percent_off, duration=duration, name=name)
        obj.id_coupon = coupon.id
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        stripe.Coupon.delete(obj.id_coupon)
        obj.delete()

    def delete_queryset(self, request, queryset):
        for discount in queryset:
            stripe.Coupon.delete(discount.id_coupon)
            discount.delete()


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Discount, DiscountAdmin)
