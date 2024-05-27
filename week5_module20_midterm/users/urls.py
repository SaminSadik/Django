from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout, name='logout'),
    path('update/', views.edit_info, name='edit_info'),
    path('password/', views.edit_pass, name='edit_pass'),
    path('LOGIN/', views.unauthorized, name='unauthorized'),
]