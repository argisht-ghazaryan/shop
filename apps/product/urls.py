from django.urls import path
from apps.product import views


urlpatterns = [
    path('ditail/', views.ditail_view, name='ditail'),
    path('add_page/', views.add_product_view, name='add_page'),
    path('update/<int:pk>/', views.update_product_view, name='update'),
    path('delete/<int:pk>/', views.delete_product_view, name='delete'),
]
