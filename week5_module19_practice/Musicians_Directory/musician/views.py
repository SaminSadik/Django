from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician

from django import dispatch
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddMusician(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class EditMusician(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('home')