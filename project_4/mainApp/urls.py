from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.Class_Based_Create.as_view(), name='createView'),
    # class based view needs to be in this format (.asview() in the end)
    path('update/<int:id>', views.Class_Based_Update.as_view(), name='updateView'),
    path('delete/<int:id>', views.Class_Based_Delete.as_view(), name='deleteView'),
    path('details/<int:pk>', views.Class_Based_Details.as_view(), name='detailsView'),
]