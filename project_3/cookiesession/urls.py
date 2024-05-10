from django.urls import path
from . import views

urlpatterns = [
    path('',views.cookies, name='cookies'),
    path('set/',views.set_cookie, name='set_cookie'),
    path('get/',views.get_cookie, name='get_cookie'),
    path('del/',views.del_cookie, name='del_cookie'),
]