from django.db import models
from django_google_maps.fields import AddressField, GeoLocationField

# Create your models here.
class Hood(models.Model):
    address = AddressField(max_length=100)
    location = GeoLocationField(blank=True)

    def __str__(self):
        return self.address