from django import forms # importing forms API
from django.core import validators # for using builtin form validators

class apiForm(forms.Form): # inheriting Form frop from API in a new class
    name = forms.CharField() # if there's no label, the variable name is the label by default
    mail = forms.EmailField(label="E-Mail") # label sets the display name of the form field
    age = forms.IntegerField(initial=18) # initial sets a default value of the form field
    weight = forms.FloatField(help_text="Max Cap 99.99 KGs") # adds a text under the form field
    balance = forms.DecimalField(disabled=True, required=False) # disabled is False by default, required is True by default
    checkbox = forms.BooleanField(required=False, label="Do you agree with our terms and conditions?") 
    
    birthday = forms.CharField(widget=forms.DateInput(attrs={"type": "date", "class" : "widgeted"}))
    # shortcut: almost anything can be CharField & then specified using widget forms._
    # widget attributes can add/change html properties 
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), required=False)

    CHOICES = [('3', 'Other'), ('2', 'Female'), ('1', 'Male')]
    gender = forms.ChoiceField(choices = CHOICES) 
    # a list of tuples needs to be passed as choices in ChoiceField
    # where in each tuple 1st elements are recieved in backend & 2nd elements are shown in frontend

    CHOICES = [('1', 'Bangla'), ('2', 'English'), ('3', 'C++')]
    languages = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple ,choices = CHOICES) # widgets can also be used for styling

    file = forms.FileField(label="Upload a file", required=False)

    def clean_name(self): # checking validation conditions for individual form fields
        nameVal = self.cleaned_data['name']
        if len(nameVal) < 8:
            raise forms.ValidationError("name must have at least 8 characters")
        return nameVal
    
    def clean(self): # form validation
        cleaned_data = super().clean() # essential to validate multiple form fields in one function
        valMail = self.cleaned_data['mail']
        valName = self.cleaned_data['name']
        if len(valName) > 15:
            raise forms.ValidationError("name can't be longer than 15 characters")
        # raise works like return, so only the first raise will be shown in frontend
        if '.com' not in valMail:
            raise forms.ValidationError("email must end with .com")

    comment = forms.CharField(
                widget=forms.Textarea, required=False,
                validators=[
                    validators.MaxLengthValidator(100, message='Comment is too long'),
                    validators.MinLengthValidator(10, message='Comment is too short')
                    ]
                ) # builtin form validator example