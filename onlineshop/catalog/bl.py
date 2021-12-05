from django.core.paginator import Paginator
from django.http import Http404
from cart.models import CartProduct
from .models import Category, Product

NUMBER_OF_PRODUCTS = 25


def category_context(category_slug):
    category = Category.objects.prefetch_related('product_set').filter(slug=category_slug).first()
    if category_context is not None:
        context = {
            'single_category': category,
        }
    else:
        raise Http404

    return context


def all_products(page_number):
    products = Product.objects.all()
    paginator = Paginator(products, NUMBER_OF_PRODUCTS)
    context = {
        'products': paginator.get_page(page_number),
    }
    return context


def single_product(product_slug):
    product = Product.objects.filter(slug=product_slug).first()

    if product is None:
        raise Http404

    return product


def is_product_in_cart(product, user):
    if CartProduct.objects.filter(product=product, cart__user=user, cart__active=True).first():
        return True
    return False
