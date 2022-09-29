from django import forms
from .models import Review


class ProductReviewForm(forms.ModelForm):
    """
    Form to add or edit a review
    """
    class Meta:
        model = Review
        fields = ('review_text', 'rating')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
