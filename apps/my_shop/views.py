from django.shortcuts import render
from apps.product.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'my_shop/index.html', context={'products': products, 'title': 'Online_shop'})
