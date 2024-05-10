from django.urls import path
from . import views

urlpatterns = [
    path('cookie/',views.cookies, name='cookies'),
    path('cookie/set/',views.set_cookie, name='set_cookie'),
    path('cookie/get/',views.get_cookie, name='get_cookie'),
    path('cookie/del/',views.del_cookie, name='del_cookie'),
    path('session/',views.session, name='session'),
    path('session/set/',views.set_session, name='set_session'),
    path('session/get/',views.get_session, name='get_session'),
    path('session/del/',views.del_session, name='del_session'),
]