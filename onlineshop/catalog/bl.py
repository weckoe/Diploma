from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, request
from django.http import Http404
from cart.models import CartProduct
from .models import Category, Product, Addon


def single_category(category_slug):
    category_products = Category.objects.prefetch_related('product_set').filter(slug=category_slug).first()
    if single_category is not None:
        context = {
            'single_category': category_products,
        }
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return context


def all_products(page_number):
    products = Product.objects.all()
    paginator = Paginator(products, 25)
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

    if user.is_authenticated:
        CartProduct.objects.filter(product=product, cart__user=user, cart__active=True).first()
        return True
    return False
