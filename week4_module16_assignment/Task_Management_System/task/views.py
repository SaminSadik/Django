from django.shortcuts import render, redirect
from .forms import TaskForm
from task.models import Task

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        tasks = TaskForm(request.POST)
        if tasks.is_valid():
            tasks.save()
            return redirect('home')
    else:
        tasks = TaskForm(request.POST)    
    return render(request,'tasks.html',{'form':tasks})

def edit_task(request, id):
    task = Task.objects.get(pk=id)
    tasks = TaskForm(instance=task)
    if request.method == 'POST':
        tasks = TaskForm(request.POST, instance=task)
        if tasks.is_valid():
            tasks.save()
            return redirect('home')
    return render(request,'tasks.html',{'form':tasks})

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')