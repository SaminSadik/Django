from django.shortcuts import render
from . forms import apiForm

# Create your views here.
def formHTML(request):
    if request.method == "POST":
        selected = request.POST.get("singleChoice")
        username = request.POST.get("name")
        return render(request, "form1.html", {"selected": selected, "username": username})
    return render(request, "form1.html")

def formDjango(request):
    form = apiForm(request.POST) # request.POST stores the input data
    print(form) # shows the WHOLE html code in console
    if form.is_valid(): # must need for using cleaned_data with request.POST
        print(form.cleaned_data) # only shows the inputs on console
    return render(request, "form2.html", {"form": form})

def formModel(request):
    return render(request, "form3.html")
