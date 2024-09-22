from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from transactions.views import send_email

class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) 
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')

class UserBankAccountUpdateView(View):
    template_name = 'profile.html'
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request,'Profile Updated')
            return redirect('profile')  
        return render(request, self.template_name, {'form': form})
    
class ChangePassword(LoginRequiredMixin,PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'pass_change.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request,'Password Updated')
        send_email(self.request.user,0,'Password Reset','pass_change_mail.html')
        return super().form_valid(form)    
    