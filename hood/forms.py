from django import forms
from .models import Hood
from django_google_maps.widgets import GoogleMapsAddressWidget

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = '__all__'
        widgets = {
            'address': GoogleMapsAddressWidget,
        }