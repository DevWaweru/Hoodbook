from django.shortcuts import render, redirect
from .forms import HoodForm
from .models import Bio, Status, Business, Hood
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    title = 'Home'

    return render(request, 'index.html',{
        'title':title,
    })

def profile(request, username):
    title = f'@{username}'

    statuses = Status.status_by_user(username)
    profile = Bio.get_bio_by_user(username)

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
        'profile':profile,
        'statuses':statuses,
    })
