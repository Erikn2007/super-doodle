from django.urls import path
from app_lesson_4 import views

urlpatterns = [
    path('', views.index, name='lesson_4'),
]

