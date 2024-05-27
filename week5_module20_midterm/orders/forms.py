from django import forms
from .models import OrderModel

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['contact_number', 'delivery_address']
        widgets = {'delivery_address': forms.Textarea(attrs={'rows': 2})}