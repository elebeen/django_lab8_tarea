from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('api/products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('api/categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('api/supliers/', views.SuplierListCreateView.as_view(), name='suplier-list-create'),
    path('api/supliers/<int:pk>/', views.SuplierDetailView.as_view(), name='suplier-detail'),

    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),

    path('supliers/', views.SuplierListView.as_view(), name='suplier-list'),
    path('supliers/create/', views.SuplierCreateView.as_view(), name='suplier-create'),
    path('supliers/<int:pk>/edit/', views.SuplierUpdateView.as_view(), name='suplier-edit'),
    path('supliers/<int:pk>/delete/', views.SuplierDeleteView.as_view(), name='suplier-delete'),
    path('supliers/<int:pk>/', views.SuplierDetailView.as_view(), name='suplier-detail'),

]