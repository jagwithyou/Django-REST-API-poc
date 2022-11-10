from django.db import models

class UserModel(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length = 180)
    last_name = models.CharField(max_length = 180)
    age = models.CharField(max_length = 180)
    street_no = models.CharField(max_length = 180)
    street = models.CharField(max_length = 180)
    city = models.CharField(max_length = 180)
    country = models.CharField(max_length = 180)

    def __str__(self):
        return self.first_name

class Car(models.Model):
    number_plate = models.IntegerField(primary_key=True)
    model = models.CharField(max_length = 180)
    brand = models.CharField(max_length = 180)
    c_id = models.CharField(max_length = 180)

    def __str__(self):
        return self.number_plate

class Ads(models.Model):
    a_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 180)
    description = models.CharField(max_length = 180)
    price_per_km = models.CharField(max_length = 180)

    def __str__(self):
        return self.title