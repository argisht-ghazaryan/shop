from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart


@login_required
def add_to_cart(request, product_id):
    cart_item = Cart.objects.filter(user=request.user, product_id=product_id).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")

    else:
        Cart.objects.create(user=request.user, product_id=product_id)
        messages.success(request, "Item added to your cart")

    return redirect("cart:cart_detail")
    # return render(request, 'cart/add_to_cart.html')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("cart:cart_detail")
    # return render(request, 'cart/remove_from_cart.html')


@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.product.amount for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, "cart/cart_ditail.html", context=context)

