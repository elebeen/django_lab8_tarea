from django import forms # type: ignore
from .models import Product, Category, Suplier

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'suplier']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SuplierForm(forms.ModelForm):
    class Meta:
        model = Suplier
        fields = ['name', 'contact_info']