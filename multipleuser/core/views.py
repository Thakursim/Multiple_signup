from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from core.serializers import (
    SellerCustomRegistrationSerializer, BuyerCustomRegistrationSerializer
    )

# Create your views here.
class SellerRegistrationView(RegisterView):
    serializer_class = SellerCustomRegistrationSerializer


class BuyerRegistrationView(RegisterView):
    serializer_class = BuyerCustomRegistrationSerializer