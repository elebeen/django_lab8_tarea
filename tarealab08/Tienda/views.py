from django.urls import reverse_lazy # type: ignore
from .serializer import CategorySerializer, ProductSerializer, SuplierSerializer  
from .models import Product, Suplier, Category
from rest_framework import generics # type: ignore
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView # type: ignore
from .forms import ProductForm, CategoryForm, SuplierForm
# Create your views here.

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SuplierListCreateView(generics.ListCreateAPIView):
    queryset = Suplier.objects.all()
    serializer_class = SuplierSerializer

class SuplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Suplier.objects.all()
    serializer_class = SuplierSerializer

# products views

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/form.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/form.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/confirm_delete.html'
    success_url = reverse_lazy('product-list')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'

# categories views

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/confirm_delete.html'
    success_url = reverse_lazy('category-list')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'

# supliers views

class SuplierListView(ListView):
    model = Suplier
    template_name = 'supliers/list.html'
    context_object_name = 'supliers'

class SuplierCreateView(CreateView):
    model = Suplier
    form_class = SuplierForm
    template_name = 'supliers/form.html'
    success_url = reverse_lazy('suplier-list')

class SuplierUpdateView(UpdateView):
    model = Suplier
    form_class = SuplierForm
    template_name = 'supliers/form.html'
    success_url = reverse_lazy('suplier-list')

class SuplierDeleteView(DeleteView):
    model = Suplier
    template_name = 'supliers/confirm_delete.html'
    success_url = reverse_lazy('suplier-list')

class SuplierDetailView(DetailView):
    model = Suplier
    template_name = 'supliers/detail.html'