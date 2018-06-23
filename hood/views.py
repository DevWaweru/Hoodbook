from django.shortcuts import render, redirect
# from .forms import CityAdminForm

# Create your views here.
def home(request):
    title = 'Home'

    # if request.method == 'POST':
    #     form = CityAdminForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         map_point = form.save(commit=False)
    #         map_point.save()
    #         return redirect('home')
    # else:
    #     form = CityAdminForm()

    return render(request, 'index.html',{
        'title':title,
        # 'form':form,
    })