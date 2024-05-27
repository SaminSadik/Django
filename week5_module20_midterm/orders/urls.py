from django.urls import path
from . import views

urlpatterns = [
    path('<slug:car_slug>/', views.Order, name='order')
]