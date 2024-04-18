from django import forms # importing forms API

class apiForm(forms.Form): # inheriting Form frop from API in a new class
    name = forms.CharField() # if there's no label, the variable name is the label by default
    mail = forms.EmailField(label="E-Mail")
    age = forms.IntegerField(label="Age")
    weight = forms.FloatField(label="Weight")
    balance = forms.DecimalField(label="Balance")
    checkbox = forms.BooleanField(label="Do you agree with our terms and conditions?")
    birthday = forms.DateField(label="Date of Birth (YY-MM-DD)")
    appointment = forms.DateTimeField(label="Appointment (YY-MM-DD hh:mm:ss)")

    CHOICES = [('3', 'Other'), ('2', 'Female'), ('1', 'Male')]
    gender = forms.ChoiceField(choices = CHOICES)
    # a list of tuples needs to be passed as choices in CHoiceField
    # where in each tuple 1st elements are recieved in backend & 2nd elements are shown in frontend

    CHOICES = [('1', 'Python'), ('2', 'Javascript'), ('3', 'C++'), ('4', 'Java'), ('5', 'C#')]
    langs = forms.MultipleChoiceField(choices = CHOICES, label="Known Programming Languages")
