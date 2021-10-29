from django.db.models import Count

from .models import Category


def nav_items_processor(request):
    categories = Category.objects.annotate(products=Count("product"))
    context = {
        'nav_items': categories,
    }
    return context
