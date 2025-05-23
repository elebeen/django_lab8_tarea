from django.urls import reverse_lazy # type: ignore
from .serializer import CategorySerializer, ProductSerializer, SuplierSerializer  
from .models import Product, Suplier, Category
from rest_framework import generics # type: ignore
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView # type: ignore
from .forms import ProductForm, CategoryForm, SuplierForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.

class IndexView(APIView):
    
    def get(self,request, format=None):
        context = {
            'products': {
                'list_create': reverse('product-list-create', request=request, format=format),
                'detail': reverse('product-detail', args=[1], request=request, format=format),  # Ejemplo con ID 1
            },
            'categories': {
                'list_create': reverse('category-list-create', request=request, format=format),
                'detail': reverse('category-detail', args=[1], request=request, format=format),
            },
            'supliers': {
                'list_create': reverse('suplier-list-create', request=request, format=format),
                'detail': reverse('suplier-detail', args=[1], request=request, format=format),
            },
            'mensaje':{'servidor activo'}
        }

        return Response(context)

class ProductApiListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class CategoryApiListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SuplierApiListCreateView(generics.ListCreateAPIView):
    queryset = Suplier.objects.all()
    serializer_class = SuplierSerializer

class SuplierApiDetailView(generics.RetrieveUpdateDestroyAPIView):
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