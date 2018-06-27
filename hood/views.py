from django.shortcuts import render, redirect
from .forms import HoodForm
# Create your views here.

def home(request):
    title = 'Home'

    return render(request, 'index.html',{
        'title':title,
    })

def profile(request):
    title = 'Profile'

    if request.method == 'POST':
        form = HoodForm(request.POST)
        if form.is_valid():
            geolocate = form.save(commit=False)
            geolocate.save()
    else:
        form = HoodForm()

    return render(request, 'profile/profile.html',{
        'title':title,
        'form':form,
    })
