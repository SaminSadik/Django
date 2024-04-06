# This file is not automatically created by default, unlike others

from django.urls import path
from . import views # for using functions from app views.py

urlpatterns = [
    path('', views.home), # accessible from projectURL/appName/
    path('temp/', views.template), # accessible from projectURL/appName/temp/
    path('stic/', views.static), # for static pages
    path('utag/', views.utag, name='utag'), # name is used to access from html file
    path('utag/page/<int:id>/', views.urltag, name='urltag'), #must have .../page/anyINT/ to access
    path('inherited/', views.inherited)
]