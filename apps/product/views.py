from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ProductForm()

    return render(request, 'product/add_product.html', context={'form': form, 'title': 'Add Page'})


def ditail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'title': f'{product.name} Ditail'
    }
    return render(request, 'product/ditail.html', context=context)


def update_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('ditail')
    return render(request, 'product/update.html', context={'form': form, 'pk': product.pk,
                                                           'title': f'UPDATE{product.name}'})


def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('ditail')
    return render(request, 'product/delete.html', context={'pk': product.pk, 'title': f'DELETE{product.name}'})
