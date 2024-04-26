from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model= models.Student
        fields = '__all__'
        labels = {
            'date' : 'Date of Birth',
            'time' : 'Time of Registration',
            'duration' : 'Jailtime Duration',
            'null_boolean_field' : 'Married?',
            'url_field' : 'Social Link'
        }
        widgets = {
            'name' : forms.TextInput()
        }
        help_texts = {
            'address' : 'Enter Your Present or Permanent Address'
        }
        error_messages = {
            'name' : {'required' : 'Name is required to proceed'}
        }