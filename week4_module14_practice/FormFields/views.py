from django.shortcuts import render
from .forms import form1

# Create your views here.
def FormFields(request):
    if request.method == 'POST':
        form = form1(request.POST , request.FILES)
        if form.is_valid():
            file=form.cleaned_data['file']
            with open('./FormFields/upload/' + file.name, 'wb+') as desination:
                for chunk in file.chunks():
                    desination.write(chunk)
            print(form.cleaned_data)       
    else:
        form = form1()
    return render(request, 'indexF.html', {'form':form})