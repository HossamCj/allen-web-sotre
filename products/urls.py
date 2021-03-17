from django.urls import path

from .views import products_list, product_details, product_add, product_edit


urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('products/add-product/', product_add, name='product_add'),
    path('products/<int:pk>/', product_details, name='product_details'),
    path('products/edit/<int:pk>/', product_edit, name='product_edit'),
]