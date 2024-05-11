from django.shortcuts import render, redirect
from .forms import signupForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView


class signup(CreateView):
  model = User 
  form_class = signupForm
  template_name = 'signup.html'
  def get_success_url(self): 
        return reverse_lazy('signin')
  def form_valid(self, form):
    messages.success(self.request, 'Account created successfully')
    return super().form_valid(form)
  def dispatch(self, request, *args, **kwargs): 
        if request.user.is_authenticated:
            messages.warning(request, 'You are already signed in')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class signin(LoginView):
    template_name ='signin.html'
    def get_success_url(self): 
        return reverse_lazy('home')
    def form_valid(self, form): 
        messages.success(self.request, 'Sign in Successful')
        return super().form_valid(form)
    def dispatch(self, request, *args, **kwargs): 
        if request.user.is_authenticated:
            messages.warning(request, 'You are already signed in')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch') 
class signout(LogoutView):
    http_method_names = ['get'] 
    def get(self, request):
        logout(request)
        messages.success(request, 'Sign out Successful')
        return redirect('signin')
    
