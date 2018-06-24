from django.db import models
from djgeojson.fields import PolygonField

# Create your models here.
class MushroomSpot(models.Model):

    title = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='p', blank=True)
    geom = PolygonField(blank=True)

    def __str__(self):
        return self.title
