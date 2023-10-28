from .models import Customer, Coupon, CustomerCoupon
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CouponList(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponListSerializer
    
    
class CouponRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponListSerializer

class CustomerCouponList(generics.ListAPIView):
    queryset = CustomerCoupon.objects.all()
    serializer_class = CustomerCouponSerializer
    
class ApplyCoupon(generics.CreateAPIView):
    queryset = CustomerCoupon.objects.all()
    serializer_class = CustomerCouponSerializer
    
    def create(self, request, *args, **kwargs):
        coupon_code = request.data.get('coupon')
        customer = request.data.get('customer')
        try:
            coupon = Coupon.objects.get(code=coupon_code, is_active=True)
            customer = Customer.objects.get(id=customer)
        except Coupon.DoesNotExist:
            return Response({'detail': 'Invalid coupon code'}, status=400)
        
        # Check if the user has already applied this coupon
        if not CustomerCoupon.objects.filter(customer=customer, coupon=coupon).exists():
            customer_coupon = CustomerCoupon(customer=customer, coupon=coupon, applied=True)
            customer_coupon.save()
            return Response({'detail': 'Coupon applied successfully'}, status=201)
        else:
            return Response({'detail': 'Coupon already applied by this user'}, status=400)

    
class CustomerCouponRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerCoupon.objects.all()
    serializer_class = CustomerCouponSerializer

