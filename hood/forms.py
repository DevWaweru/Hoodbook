from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from .models import Hood
from django import forms

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('name','coordinates','city_hall')
        widgets = {
            'coordinates': GooglePointFieldWidget,
            'city_hall': GooglePointFieldWidget,
        }