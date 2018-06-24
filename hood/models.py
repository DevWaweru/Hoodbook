from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.
class PointOfInterest(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    position = GeopositionField(blank=True)

    # class Meta:
    #     verbose_name_plural = 'points of interest'