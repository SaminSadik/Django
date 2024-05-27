from .forms import signupForm, ProfileForm, PassForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from orders.models import OrderModel

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('profile')
    if(request.method == 'POST'):
        form = signupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
            return redirect('login')
    else:
        form = signupForm()
        messages.info(request, 'Welcome to Signup Page')
    return render(request, 'signup.html', {'form': form})


class Login(LoginView):
    template_name ='login.html'
    def get_success_url(self): 
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Login Successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Login Failed')
        return super().form_invalid(form)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'You are already logged in')
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)


@login_required
def Logout(request):
    logout(request) 
    messages.success(request, 'You are now logged out')
    return redirect('login')


@login_required
def profile(request):
    user = request.user
    orders = OrderModel.objects.filter(user=user)
    return render(request, 'profile.html', {'user':user, 'orders':orders})


@login_required 
def edit_info(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'edit.html', {'form':form})


@login_required 
def edit_pass(request):
    if request.method == 'POST':
        form = PassForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PassForm(user=request.user)
    return render(request, 'edit.html', {'form':form})


def unauthorized(request):
    messages.warning(request, 'You need to login first to access that!')
    return redirect('login')
    