from . import views
from django.urls import path

urlpatterns = [
    path('', views.ModelFields, name="ModelFields"),
    path('delete/<int:roll>', views.delete_student, name= 'delete_student')
]