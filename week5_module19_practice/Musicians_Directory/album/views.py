from .forms import AlbumForm
from .models import Album
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class add_album(CreateView):
  model = Album
  form_class = AlbumForm
  template_name = 'add_album.html'
  success_url = '/' 

@method_decorator(login_required, name='dispatch')
class edit_album(UpdateView):
  model = Album
  form_class = AlbumForm
  template_name = 'add_album.html'
  success_url = '/' 

@method_decorator(login_required, name='dispatch')
class delete_album(DeleteView):
    model = Album
    template_name = 'delete_album.html'
    success_url = '/'