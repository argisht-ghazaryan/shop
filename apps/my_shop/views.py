from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from apps.my_shop.forms import SearchForm
from apps.product.models import Product, Categories
from django.core.paginator import Paginator


def home(request):
    products = Product.objects.all().order_by('pk')
    cats = Categories.objects.all()
    # paginator = Paginator(products, 3)
    # page_number = request.GET.get("page")
    # products = paginator.get_page(page_number)
    return render(request, 'my_shop/index.html', context={'products': products, 'cats': cats, 'title': 'Online_shop'})


def categories_list(request):
    cats = Categories.objects.all()
    return render(request, 'base.html', context={'cats': cats})


def category_by_id(request, pk):
    cat = get_object_or_404(Categories, id=pk)
    cats = Categories.objects.all()
    return render(request, 'base.html', context={'cat': cat, 'cats': cats})


def category_products(request, pk):
    cat = Product.objects.filter(categories=pk)
    return render(request, 'product/category_products.html', context={'cat': cat})


def search(request):
    products = []
    form = SearchForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(model__icontains=search_query) |
                                          Q(color__icontains=search_query) | Q(categories__name=search_query))
    return render(request, 'my_shop/search.html', context={'form': form, 'products': products})
