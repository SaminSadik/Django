from django.shortcuts import redirect
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View

# Create your views here.
class Signin(LoginView):
    template_name = 'user_signin.html'
    def get_success_url(self):
        return reverse_lazy('home')

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'user_signup.html'
    success_url = reverse_lazy('user_signin')

class Signout(View):
    def get(self, request):
        logout(request)
        return redirect('user_signin')