from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm

class signupForm(UserCreationForm): # inheriting in-built form for user creation
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User # imported in-built model
        # fields = '__all__' # it has a lot of fields a general user shouldn't access
        fields = ['first_name', 'last_name', 'username', 'email']
        # password fields will be included automatically even if not specified

class ProfileForm(UserChangeForm): # in-built for changing user info
    password = None # otherwise password field would appear despite not being in fields
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {'username' : None}

class PassForm1(PasswordChangeForm): # in-built for changing password with old password
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
        
class PassForm2(SetPasswordForm):  # in-built for changing password without old password
    new_password1 = forms.CharField (label='New password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'