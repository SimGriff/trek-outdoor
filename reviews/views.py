from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from .models import Review


@login_required
def add_review(request, product_id):
    """ To add a product review """

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                review = form.save()
                review.user = request.user
                review.product = product
                review.save()
                messages.success(request, f'Your review for {product.name} has been added')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    context = {
        'form': form,
        'product': product
    }

    return render(request, context)


@login_required
def edit_review(request, product_id, review_id ):
    """ To edit a product review """

    review = get_object_or_404(Review, pk=product_id)
    product = review.product

    if request.user.is_authenticated:

        if request.method == 'POST':
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                review = form.save()
                review.user = request.user
                review.product = product
                review.save()
                messages.success(request, f'Successfully updated review for {product.name}')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to update the review. Please ensure the form is valid.')
    else:
        form = ProductReviewForm(instance=review)

    context = {
        'review': review,
        'form': form,
        'product': product,
    }

    return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, product_id, review_id ):
    """ To delete a product review """

    review = get_object_or_404(Review, pk=product_id)
    product = review.product

    review.delete()
    
    messages.success(request, f'Deleted review for {product.name}')
    return redirect(reverse('product_detail', args=[product.id]))
