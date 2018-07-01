from django.shortcuts import render, redirect
from .forms import HoodForm, StatusForm, BioForm, BusinessForm
from .models import Bio, Status, Business, Hood
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    title = 'Home'
    # Get users hood
    profile = Bio.get_bio_by_user(request.user)
    print(profile.user_hood.name)

    # Display all statuses from the hood
    statuses = Status.status_by_hood(profile.user_hood.name)

    #Create form for posting status
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            status.user = request.user
            status.hood = profile.user_hood
            status.save()
    else:
        form = StatusForm()

    return render(request, 'index.html',{
        'title':title,
        'profile':profile,
        'form': form,
        'statuses':statuses
    })

def profile(request, username):
    title = f'@{username}'

    statuses = Status.status_by_user(username)
    profile = Bio.get_bio_by_user(username)

    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            status.user = request.user
            status.hood = profile.user_hood
            status.save()
    else:
        form = StatusForm()

    return render(request, 'profile/profile.html',{
        'title':title,
        'form':form,
        'profile':profile,
        'statuses':statuses,
    })

def update_location(request):
    title = 'Update Location'

    if request.method == 'POST':
        form = HoodForm(request.POST)
        if form.is_valid():
            geolocate = form.save(commit=False)
            geolocate.save()
    else:
        form = HoodForm()

    return render(request, 'update.html', {
        'title':title,
        'form':form,
        })