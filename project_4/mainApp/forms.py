from django import forms
from .models import mainModel, extraModel

class mainForm(forms.ModelForm):
    class Meta:
        model = mainModel
        exclude = ['owner']

class extraForm(forms.ModelForm):
    class Meta:
        model = extraModel
        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'rows': 3})}