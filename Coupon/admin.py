from django.contrib import admin
from .models import Customer, Coupon, CustomerCoupon
# Register your models here.3



admin.site.register(Customer)
admin.site.register(Coupon)
admin.site.register(CustomerCoupon)
