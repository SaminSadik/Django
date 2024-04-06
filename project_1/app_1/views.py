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

def static(request):
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },{
            "userId": 1,
            "id": 2,
            "title": "qui est esse",
            "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
        },{
            "userId": 1,
            "id": 3,
            "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
            "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
        }
    ] # from: https://jsonplaceholder.typicode.com/posts

    return render(request, "app_1/static.html", {'data' : data})

def urltag(request, id):
    return render(request, "app_1/URLtag.html", {'id' : id})
    # passed the id recieved from urls to html page

def utag(request):
    return render(request, "app_1/URLtag.html", {'input' : request.GET})
    # passed anything GOT after .../utag/? as url input

def inherited(request):
    return render(request, "app_1/inherit/inherited.html")