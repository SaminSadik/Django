from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
# def add_musician(request):
#     if request.method=='POST':
#         musicianForm = MusicianForm(request.POST)
#         if musicianForm.is_valid():
#             musicianForm.save()
#             return redirect('home')
#     else:
#         musicianForm = MusicianForm(request.POST)
        
#     return render(request, 'add_musician.html', {'form':musicianForm})


# def edit_musician(request, id):
#     musician = Musician.objects.get(pk=id)
#     musicianForm = MusicianForm(instance=musician)
#     if request.method=='POST':
#         musicianForm = MusicianForm(request.POST, instance=musician)
#         if musicianForm.is_valid():
#             musicianForm.save()
#             return redirect('home')
        
#     return render(request, 'add_musician.html', {'form':musicianForm})

@method_decorator(login_required, name='dispatch')
class add_musician(CreateView):
  model = Musician
  form_class = MusicianForm
  template_name = 'add_musician.html'
  success_url = '/' 

@method_decorator(login_required, name='dispatch')
class edit_musician(UpdateView):
  model = Musician
  form_class = MusicianForm
  template_name = 'add_musician.html'
  success_url = '/' 
