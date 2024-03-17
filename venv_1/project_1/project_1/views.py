# This file is not automatically created by default, unlike others

from django.http import HttpResponse

def contact(request):
    return HttpResponse("This is the contact page")
def homepage(request):
    return HttpResponse("This is the homepage")