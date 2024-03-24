from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    d = {'Name' : 'San', 'Age' : 21,
         'Dict' : [
             {'id':1, 'Title':'Python'},
             {'id':2, 'Title':'HTML'}
            ],
         'Datetime' : datetime.datetime.now(),
         'OldDate' : datetime.date(year=2003, month=3, day=20),
         'NewDate' : datetime.date(year=2023, month=3, day=20)
        }
    return render (request, 'index.html',d)