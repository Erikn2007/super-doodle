from django.shortcuts import render
from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='main-page'),
    path('top-sellers/', topSellers, name='top-sellers'),
    path('adv-post/', advertPost, name='adv-post'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
]
