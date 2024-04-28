from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

from django import dispatch
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name ='add_album.html'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class EditAlbum(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name ='add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class DeleteAlbum(DeleteView):
    model = Album
    template_name = 'delete_album.html'
    pk_url_kwarg= 'id'
    success_url = reverse_lazy('home')