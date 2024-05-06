from django.shortcuts import render, redirect
from . import models, forms
from app4relations.forms import Relation_Form
from app4relations.models import relationModel, exampleModel

def Model(request):
    data = models.myModel.objects.all() # for passing all object data to the template
    return render(request, 'model.html', {'data': data})


def add(request):
    if request.method == "POST":
        form = forms.Model_Form(request.POST) # getting form with entries
        if form.is_valid():
            form.save() # saving the form entry into the database
            return redirect('Model')
    else:
        form = forms.Model_Form()
    return render(request, 'model.html', {'form': form})


def delete(request, id):
    models.myModel.objects.get(pk=id).delete() # deletes the specified object
    return redirect('Model')


def edit(request, id):
    data = models.myModel.objects.get(pk=id) # getting the object with the specified id
    if request.method == "POST":
        form = forms.Model_Form(request.POST, instance=data) # getting form with entries & instance
        if form.is_valid():
            form.save()
            return redirect('Model')
    else:
        form = forms.Model_Form(instance=data)  # getting the form with just the object data
    return render(request,'model.html', {'form': form})

def relations(request, SLUG = None):
    data = relationModel.objects.all() # for passing all object data to the template
    if request.method == "POST":
        form = Relation_Form(request.POST) # getting form with entries
        if form.is_valid():
            form.save() # saving the form entry into the database
            return redirect('relations')
    else:
        form = Relation_Form()

    if SLUG is not None: # in function None is passed if no SLUG is specified
        sort = exampleModel.objects.get(slug=SLUG) # getting the object with the specified slug
        data = relationModel.objects.filter(speciality=sort) # filtering a field with specific value
        # 'slug' & 'speciality' aren't keywords, but required field names

    return render(request, 'relations.html', {'form': form,'data': data})

def unrelate(request, id):
    relationModel.objects.get(pk=id).delete()
    return redirect('relations')
