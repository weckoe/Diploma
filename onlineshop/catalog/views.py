from django.shortcuts import render
from django.contrib.auth import get_user_model
from .bl import category_context, all_products, single_product, is_product_in_cart

User = get_user_model()


def home(request):
    page_number = request.GET.get('page')
    context = all_products(page_number)
    return render(request, 'home_page.html', context)


def categories_view(request, category_slug):
    context = category_context(category_slug)
    return render(request, 'single_category.html', context)


def single_product_view(request, product_slug):
    product = single_product(product_slug)
    is_in_cart = is_product_in_cart(product, request.user)
    context = {
        'single_product': product,
        'is_in_cart': is_in_cart,
    }
    return render(
        request,
        'single_product.html',
        context
    )
