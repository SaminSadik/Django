from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the app homepage")

def about(request):
    return HttpResponse("This is the about page")
