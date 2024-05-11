from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_album.as_view(), name='add_album'),
    path('edit/<int:pk>', views.edit_album.as_view(), name='edit_album'),
    path('delete/<int:pk>', views.delete_album.as_view(), name='delete_album'),
]