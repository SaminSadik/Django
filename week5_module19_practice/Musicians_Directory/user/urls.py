from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.Signin.as_view(), name='user_signin'),
    path('signup/', views.SignUp.as_view(), name='user_signup'),
    path('signout/', views.Signout.as_view(), name='user_signout')
]