from rest_framework import  serializers
from .models import UserModel, Ads, Car

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
