from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        
class CouponListSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"

class CustomerCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCoupon
        fields = '__all__'
        