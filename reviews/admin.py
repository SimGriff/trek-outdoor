from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):

    model = Review
    list_display = (
        'product',
        'user',
        'rating',
        'review_text',
        'date',
    )

    ordering = ('-product', '-date')
    list_filter = ('rating',)

admin.site.register(Review, ReviewAdmin)
