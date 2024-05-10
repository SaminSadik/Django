from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    # path('signin/', views.signin, name='signin'),
    path('signin/', views.class_based_signin.as_view(), name='signin'),
    # path('signout/', views.signout, name='signout'),
    path('signout/', views.class_based_signout.as_view(), name='signout'),
    path('edit_info/', views.edit_info, name='edit_info'),
    path('edit_pass/', views.edit_pass, name='edit_pass')
]