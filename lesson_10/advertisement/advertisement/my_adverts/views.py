from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement
# Create your views here.
def index(request):
    adverts = Advertisement.objects.all()
    context = {'adverts': adverts}
    return render(request, 'index.html', context)
def topSellers(request):
    return render(request, 'top-sellers.html')
def advertPost(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
        else:
            return render(request, 'advertisement-post.html', {'form': form})
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
def profile(request):
    return render(request, 'profile.html')






