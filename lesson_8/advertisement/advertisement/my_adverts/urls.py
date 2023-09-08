from django.shortcuts import render
from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='main_page'),
    path('top-sellers.html', topSellers, name='top-sellers'),
    path('advertisement-post.html', advertisementpost, name='advertisement-post'),
    path('register.html', register, name='register'),
    path('login.html', login, name='login'),
    path('profile.html', profile, name='profile'),
]
