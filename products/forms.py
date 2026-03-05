from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            'image':forms.FileInput(attrs={'class':'form-control bg-secondary m-1'}),
            'name':forms.TextInput(attrs={'class':'form-control m-2'}),
            'price':forms.NumberInput(attrs={'class':'form-control m-2'}),
            'category':forms.RadioSelect(attrs={'class':' m-2'}),
            'description':forms.Textarea(attrs={'class':'form-control m-2'}),

        }