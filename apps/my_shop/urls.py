from django.urls import path
from .views import home, categories_list, category_by_id, category_products, search


urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories_list, name='categories'),
    path('category/<pk>/', category_by_id, name='category'),
    path('category_producrs/<int:pk>/', category_products, name='cat_products'),
    path('search/', search, name='search'),

]
