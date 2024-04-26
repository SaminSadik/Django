from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician

# Create your views here.
def add_musician(request):
    if request.method=='POST':
        musicianForm = MusicianForm(request.POST)
        if musicianForm.is_valid():
            musicianForm.save()
            return redirect('home')
    else:
        musicianForm = MusicianForm(request.POST)
        
    return render(request, 'add_musician.html', {'form':musicianForm})


def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    musicianForm = MusicianForm(instance=musician)
    if request.method=='POST':
        musicianForm = MusicianForm(request.POST, instance=musician)
        if musicianForm.is_valid():
            musicianForm.save()
            return redirect('home')
        
    return render(request, 'add_musician.html', {'form':musicianForm})
