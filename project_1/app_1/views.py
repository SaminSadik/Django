from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    return render(request, "app_1/appHome.html") # for loading html page

def template(request):
    # Context (passing something from backend to frontend):
    d = {'Name' : 'San', 'Age' : 21,
         'Dict' : [
             {'id':1, 'Title':'Python'},
             {'id':2, 'Title':'HTML'}
            ],
         'Datetime' : datetime.datetime.now(),
         'Birthday' : datetime.date(year=2003, month=3, day=20)
        }
    # can be passed as an key-value pair (dictionary)
    return render(request, "app_1/template.html", d) # passing context
    # return render(request, "app_1/template.html", context={'Name' : 'San', 'Age' : 21})
