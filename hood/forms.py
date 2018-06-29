from django import forms
from .models import Hood, Status, Bio, Business
from django_google_maps.widgets import GoogleMapsAddressWidget

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = '__all__'
        widgets = {
            'address': GoogleMapsAddressWidget,
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'
        exclude = ['date_added']

class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = '__all__'
        exclude = ['user']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        exclude = ['hood','user','date_posted']