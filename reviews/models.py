from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """
    A product review and rating model
    """
    RATING = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING, null=False, blank=False)
    review_text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product}'
