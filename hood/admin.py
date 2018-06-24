from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import MushroomSpot

# Register your models here.
admin.site.register(MushroomSpot, LeafletGeoAdmin)