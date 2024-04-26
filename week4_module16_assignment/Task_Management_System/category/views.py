from django.shortcuts import render ,redirect
from .forms import CategoryForm

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        categories = CategoryForm(request.POST)
        if categories.is_valid():
            categories.save()
            return redirect('add_category')
    else:
        categories = CategoryForm(request.POST)

    return render(request,'categories.html',{'form':categories})