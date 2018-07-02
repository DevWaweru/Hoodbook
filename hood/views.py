from django.shortcuts import render, redirect
from .forms import HoodForm, StatusForm, BioForm, BusinessForm
from .models import Bio, Status, Business, Hood
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    title = 'Home'
    if request.user.is_authenticated():
        # Get users hood
        profile = Bio.get_bio_by_user(request.user)
        # print(profile.user_hood.name)

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
    else:
        return redirect('/accounts/login/')

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

@login_required(login_url='/accounts/login')
def profile_bio(request, username):
    title = 'Bio'
    profile = Bio.get_bio_by_user(username)

    if request.method == 'POST':
        bio_form = BioForm(instance = request.user.bio, data=request.POST)
        if bio_form.is_valid():
            bio_form.save()
            # bio.user = request.user

        hood_form = HoodForm(request.POST)
        if hood_form.is_valid():
            geolocate = form.save(commit=False)
            geolocate.save()
    else:
        bio_form = BioForm()
        hood_form = HoodForm()


    return render(request, 'profile/bio.html', {
        'title':title,
        'form':bio_form,
        'hood_form':hood_form,
        'profile':profile,
    })

@login_required(login_url='/accounts/login')
def profile_business(request, username):
    title = 'Business'
    profile = Bio.get_bio_by_user(username)

    return render(request, 'profile/business.html', {
        'title':title,
        'form':form,
        'profile':profile,
    })