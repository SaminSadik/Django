from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('form1/', views.formHTML),
    path('form2/', views.formDjango),
]