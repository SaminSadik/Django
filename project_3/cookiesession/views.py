from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def cookies(request):
    return render(request, 'cookies.html')
def session(request):
    return render(request,'session.html')

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

def set_session(request):
    request.session['code'] = '1XS0l' # setting a key-value pair to session
    data = {
        'id': 23,
        'name': 'test'
    }
    request.session.update(data) # updating a dictionary in session
    print(request.session.get_session_cookie_age()) # session expiration in seconds
    print(request.session.get_expiry_date()) # session expiration date & time
    return render(request,'set_session.html')

def get_session(request):
    #* session data is by default hashed for security purposes
    ID = request.session.get('id') # getting a session value by key
    code = request.session.get('code', 'UNKNOWN') # setting a default value if key doesn't exist
    request.session.modified = True # resets the expiration timer(set in settings.py) on refresh
    return render(request, 'get_session.html', {'code':code, 'ID':ID})

def del_session(request):
    # del request.session['code'] # deleting a specific session value by key
    request.session.flush() # deleting all session values
    return render(request, 'del_session.html')