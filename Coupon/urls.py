from django.urls import path
from .views import *

urlpatterns = [
    path('coupons/', CouponList.as_view(), name='coupon-list'),
    path('coupons/<int:pk>/', CouponRetrieveUpdateDestroyView.as_view(), name='coupon-list-retrieve-update-destroy'),
    path('apply_coupon/', ApplyCoupon.as_view(), name='apply-coupon'),
    path('applied_coupons/', CustomerCouponList.as_view(), name='customer-coupon-list'),
    path('applied_coupons/<int:pk>/', CustomerCouponRetrieveUpdateDestroyView.as_view(), name='customer-coupon-retrieve-update-destroy')
]
