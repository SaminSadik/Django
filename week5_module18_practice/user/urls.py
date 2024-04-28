from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('signup/', views.user_signup, name='user_signup'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/changePassword1', views.changePass1, name='changePass1'),
    path('profile/changePassword2', views.changePass2, name='changePass2'),
]