from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Product, Categories
from .forms import ProductForm
from django.views.generic import UpdateView


def add_product_view(request):
    if request.method == 'POST':
        # initial_form = {'owner': user}
        form = ProductForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            # data = form.cleaned_data
            # print(type(form.cleaned_data))
            # data['owner_id'] = user.id
            # Product.objects.create(**data)
            instance = form.save(commit=False)
            instance.owner = user
            instance.save()
            return redirect('home')
    form = ProductForm()

    return render(request, 'product/add_product.html', context={'form': form, 'title': 'Add Page'})


def ditail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    all_cat_products = Product.objects.filter(categories=product.categories)
    paginator = Paginator(all_cat_products, 4)
    page_number = request.GET.get("page")
    cat_list = paginator.get_page(page_number)
    price_off = product.amount - (product.amount * 20) // 100

    if request.method == "POST":
        messages.success(request, f"{product.name} added to your cart.")
        return redirect("cart:add_to_cart", product_id=product.id)

    context = {
        'product': product,
        'title': f'{product.name} Ditail',
        'price_off': price_off,
        'cat_list': cat_list,
    }
    return render(request, 'product/ditail.html', context=context)


def update_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST' and request.user.profile.category == 'SALESMAN':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product {product.name} updated successfully')
            return redirect('home')
    return render(request, 'product/update.html', context={'form': form, 'pk': product.pk,
                                                           'title': f'UPDATE{product.name}'})


# class UpdateProduct(UpdateView):


def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'product/delete.html', context={'pk': product.pk, 'title': f'DELETE{product.name}'})


def my_products_view(request):
    my_products = []
    my_cats = []
    if request.user.is_authenticated:
        user = request.user
        my_products = Product.objects.filter(owner=user)
        my_cats = Categories.objects.filter(product__owner=user)
    return render(request, 'product/my_products.html', context={'my_products': my_products, 'title': 'my_products',
                                                                'my_cats': my_cats})



