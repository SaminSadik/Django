from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signupForm(UserCreationForm): 
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User 
        fields = ['username', 'email']
