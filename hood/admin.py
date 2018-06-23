from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget
from .models import Hood
from django import forms

# Register your models here.

admin.site.register(Hood, )