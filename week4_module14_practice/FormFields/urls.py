from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormFields, name='FormFields')
]