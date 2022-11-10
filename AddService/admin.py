from django.contrib import admin
from .models import Ads,Car,UserModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(Car)
admin.site.register(Ads)
