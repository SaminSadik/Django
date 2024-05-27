from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm

class signupForm(UserCreationForm): 
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class ProfileForm(UserChangeForm):
    password = None 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {'username' : None}
        
class PassForm(SetPasswordForm): 
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'