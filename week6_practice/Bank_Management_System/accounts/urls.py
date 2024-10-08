from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserBankAccountUpdateView, ChangePassword
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile'),
    path('profile/pass_change/', ChangePassword.as_view(), name='change_password' )
]