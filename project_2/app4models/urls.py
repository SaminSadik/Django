from django.urls import path
from . import views

urlpatterns = [
    path('', views.Model, name='Model'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('relations/', views.relations, name='relations'),
    path('unrelate/<int:id>', views.unrelate, name='unrelate'),
    path('relations/<slug:SLUG>', views.relations, name='slugSort'),
]
