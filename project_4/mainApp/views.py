from . import models, forms
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch') # using login_required in class
class Class_Based_Create(CreateView):
    model = models.mainModel # associated model to be used
    form_class = forms.mainForm # associated form to be passed
    template_name = 'form.html' # render destination
    success_url = reverse_lazy('home') # works like return redirect
    
    def form_valid(self, form): # form is passed from form_class
        form.instance.owner = self.request.user
        # setting a field of the form instance to the current user
        form.instance.pic = self.request.FILES.get('pic')
        # also must have enctype on html form tag for FILES to save
        return super().form_valid(form) # finally validating updated form


# accessing without logging in, redirects to LOGIN_URL of settings.py
@method_decorator(login_required, name='dispatch')
class Class_Based_Update(UpdateView):
    model = models.mainModel 
    form_class = forms.mainForm
    template_name = 'form.html' 
    success_url = reverse_lazy('home') 
    def form_valid(self, form): # only here for request.FILES
        form.instance.pic = self.request.FILES.get('pic')
        return super().form_valid(form)
    
    pk_url_kwarg = 'id' # to pass the id of the object to be updated in urls


@method_decorator(login_required, name='dispatch')
class Class_Based_Delete(DeleteView):
    model = models.mainModel 
    template_name = 'delete.html' # needs a template to submit POST form
    success_url = reverse_lazy('home') 
    pk_url_kwarg = 'id' 
    def get_context_data(self, **kwargs): # to pass context
        context = super().get_context_data(**kwargs) # for accessing default method
        context['context'] = self.object # adding key-value pair to the main class
        # access the object in the template using 'key'.fieldname
        # DeleteView class has self.object as the object to be deleted
        return context # overriding super to pass context
    

class Class_Based_Details(DetailView):
    model = models.mainModel
    template_name = 'details.html'
    # pk_url_kwarg = 'id' # not necessary if pk is directly used in urls
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = self.object # to pass entire model data as context
        context['form'] = forms.extraForm() # to pass a different form as context
        context['comments'] = self.object.comments.all()
        # getting all connection of mainModel through reverse relationship(related_name)
        return context
    def post(self, request, *args, **kwargs): # manual post handling
        form = forms.extraForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # accessing the form without saving
            comment.connection = self.get_object() # connecting obj of mainM to extraM
            comment.credit = request.user # updating necessary form fields
            comment.save() # finally saving updated form
        return self.get(request, *args, **kwargs) # redirecting to same page after post
