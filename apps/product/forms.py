from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'model', 'amount', 'currency', 'count', 'description', 'size',
                  'color', 'rate', 'photo', 'video', 'categories')
