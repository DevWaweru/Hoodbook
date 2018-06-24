from django.shortcuts import render, redirect
from .forms import HoodForm
# Create your views here.
def home(request):
    title = 'Home'

    if request.method == 'POST':
        form = HoodForm(request.POST)
        if form.is_valid():
            geolocate = form.save(commit=False)
            geolocate.save()
    else:
        form = HoodForm()

    return render(request, 'index.html',{
        'title':title,
        'form':form,
    })