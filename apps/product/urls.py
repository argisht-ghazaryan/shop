from django.urls import path
from .views import ditail_view, add_product_view, update_product_view, delete_product_view, my_products_view

app_name = 'products'
urlpatterns = [
    path('ditail/<int:pk>/', ditail_view, name='ditail'),
    path('add_product/', add_product_view, name='add_product'),
    path('update/<int:pk>/', update_product_view, name='update'),
    path('delete/<int:pk>/', delete_product_view, name='delete'),
    path('my_products/', my_products_view, name='my_products'),
]
