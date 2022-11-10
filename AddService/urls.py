from django.contrib import admin
from django.urls import path, include
from AddService import urls as user_urls
from .views import UserCreateApi, UserApi, UserUpdateApi, CarCreateApi,\
    CarApi, CarUpdateApi, AdsApi, AdsCreateApi, AdsUpdateApi

urlpatterns = [
    path('api/create',UserCreateApi.as_view()),
    path('api/',UserApi.as_view()),
    path('api/<int:pk>',UserUpdateApi.as_view()),
    path('api/car/create',CarCreateApi.as_view()),
    path('api/car/',CarApi.as_view()),
    path('api/car/<int:pk>',CarUpdateApi.as_view()),
    path('api/ads/create',AdsCreateApi.as_view()),
    path('api/ads/',AdsApi.as_view()),
    path('api/ads/<int:pk>',AdsUpdateApi.as_view()),
]
