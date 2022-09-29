from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile
from .models import Review
from .forms import ProductReviewForm


@login_required
def add_review(request, product_id):
    """ To add a product review """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = user
                review.product = product
                form.save()
                messages.success(request, f'Successfully updated review for {product.name}')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to update the review. Please ensure the form is valid.')
        else:
            form = ProductReviewForm()

        template = 'reviews/add_review.html'
        context = {
            'form': form,
            'product': product,
            'user_profile': user,
        }

        return render(request, template, context)


@login_required
def edit_review(request, product_id, review_id):
    """ To edit a product review """

    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                review = form.save()
                review.user = request.user
                review.product = product
                messages.success(request, f'Successfully updated review for {product.name}')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to update the review. Please ensure the form is valid.')
        else:
            form = ProductReviewForm()

        template = 'reviews/add_review.html'
        context = {
            'review': review,
            'form': form,
            'product': product,
        }

        return render(request, template, context)


@login_required
def delete_review(request, product_id, review_id):
    """ To delete a product review """
    if not request.user:
        messages.error(request, "You can't edit this review")
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    review.delete()
    messages.success(request, f'Deleted review for {product.name}')
    return redirect(reverse('product_detail', args=[product.id]))
