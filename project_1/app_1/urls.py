# This file is not automatically created by default, unlike others

from django.urls import path
from . import views # for using functions from app views.py

urlpatterns = [
    path('', views.home), # accessible from projectURL/appName/
]