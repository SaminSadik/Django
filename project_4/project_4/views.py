from django.shortcuts import render
from mainApp.models import mainModel
# Create your views here.
def base(request):
    data = mainModel.objects.all()
    return render(request, 'base.html', {'data': data})
