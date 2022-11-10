from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserModelSerializer, CarSerializer, AdsSerializer
from .models import UserModel, Car, Ads

class UserCreateApi(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class UserApi(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class UserUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class CarCreateApi(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarApi(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class AdsCreateApi(generics.CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class AdsApi(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class AdsUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer