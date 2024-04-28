from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'New Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',  'password1', 'password2']
        labels = {
            'username' : '',
            'first_name' : '', 
            'last_name' : '',
            'email' : '',
        }
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'Username'}),
            'first_name' : forms.TextInput(attrs={'placeholder':'First name'}),
            'last_name' : forms.TextInput(attrs={'placeholder':'Last name'}),
            'email' : forms.TextInput(attrs={'placeholder':'Email'})
        }
        help_texts = {
            'username' : None
        }

class ProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password to Save Changes'}), label='Password', required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username' : None
        }

class PassForm1(PasswordChangeForm):
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
        
class PassForm2(SetPasswordForm):
    new_password1 = forms.CharField (label='New password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'