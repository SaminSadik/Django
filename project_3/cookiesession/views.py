from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def cookies(request):
    return render(request, 'cookies.html')

def set_cookie(request):
    response = render(request, 'set_cookie.html')
    response.set_cookie('name', 'c1') # setting cookie as key-value pair
    response.set_cookie('name', 'c2', max_age=5) # max_age is expiration time in seconds
    response.set_cookie('name', 'c3', expires=datetime.now()+timedelta(days=7))
    # to use anything other than seconds as max_age, expires with datetime is used
    # previous cookies get overriden by the last
    # without max_age or expires, cookie gets deleted when session/browser is closed
    return response

def get_cookie(request):
    # print(request.COOKIES)
    name = request.COOKIES.get('name') # getting the cookie value by key
    return render(request, 'get_cookie.html', {'name':name})

def del_cookie(request):
    response = render(request, 'del_cookie.html')
    response.delete_cookie('name') # manually deleting cookie by key
    return response