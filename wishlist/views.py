from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Wishlist


@login_required
def wishlist(request):
    """
    A view to show the user's wishlist
    """
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the wishlist for the logged in user
    """
    product = get_object_or_404(Product, pk=product_id)

    # Create a wishlist for the user if they don't have one already
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    # Add a product to the wishlist
    wishlist.products.add(product)
    messages.info(request, f'{product.name} was added to your wishlist')

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the wishlist for the logged in user
    """
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from the wishlist
    wishlist.products.remove(product)
    messages.info(request, f'{product.name} has been removed from your Wishlist')

    return redirect(request.META.get('HTTP_REFERER'))
