from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup.as_view(), name='signup'),
    path('signin/', views.signin.as_view(), name='signin'),
    path('signout/', views.signout.as_view(), name='signout'),
]