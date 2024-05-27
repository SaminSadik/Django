from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3})
        }