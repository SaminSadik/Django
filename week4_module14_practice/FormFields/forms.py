from django import forms
from django.core import validators

class form1(forms.Form): # inheriting Form API in a new class
    name = forms.CharField() # if there's no label, the variable name is the label by default
    mail = forms.EmailField(label="E-Mail") # label sets the display name of the form field
    age = forms.IntegerField(initial=18, required=False) # initial sets a default value of the form field
    weight = forms.FloatField(help_text="Max Cap 99.99 KGs", required=False) # adds a text under the form field
    balance = forms.DecimalField(disabled=True, required=False) # disabled is False by default, required is True by default
    checkbox = forms.BooleanField(required=False, label="Do you agree with our terms and conditions?") 
    
    birthday = forms.CharField(widget=forms.DateInput(attrs={"type": "date"}))
    # shortcut: almost anything can be CharField & then specified using widget forms._
    # widget attributes can add/change html properties 
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), required=False)

    CHOICES = [('1', 'None'), ('2', 'C/C++'), ('3', 'Python'), ('4', 'Javascript')]
    lang = forms.ChoiceField(choices = CHOICES, label="Favorite Programming Language")
    # a list of tuples needs to be passed as choices in ChoiceField
    # where in each tuple 1st elements are recieved in backend & 2nd elements are shown in frontend
    langs = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple ,choices = CHOICES, label="Known Programming Languages")

    file = forms.FileField(label="Upload a file", required=False)
    
    comment = forms.CharField(
                widget=forms.Textarea(attrs={'rows':3}), required=False,
                validators=[
                    validators.MaxLengthValidator(100, message='Comment is too long'),
                    validators.MinLengthValidator(10, message='Comment is too short')
                    ]
            ) # builtin form validator example

    def clean(self): # manual form validation
        cleaned_data = super().clean() # essential to validate multiple form fields in one function
        valMail = self.cleaned_data['mail']
        valName = self.cleaned_data['name']
        if len(valName) > 15:
            raise forms.ValidationError("name can't be longer than 15 characters")
        # raise works like return, so only the first raise will be shown in frontend
        if '.com' not in valMail:
            raise forms.ValidationError("email must end with .com")