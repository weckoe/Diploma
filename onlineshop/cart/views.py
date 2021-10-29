from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from catalog.views import home
from .models import Cart, CartProduct, Order, Customer
from catalog.models import Product


@login_required(login_url=reverse_lazy('authentication:login'))
def add_to_cart(request, slug):
    slug_product = Product.objects.get(slug=slug)
    new_cart, _ = Cart.objects.get_or_create(user=request.user)
    new_product, _ = CartProduct.objects.get_or_create(product=slug_product, cart=new_cart)
    return home(request)


@login_required(login_url=reverse_lazy('authentication:login'))
def cart(request):
    user = request.user
    customer, _ = Customer.objects.get_or_create(user=user)
    customer.save()
    cart_id = Cart.objects.filter(user_id=user.id).first()
    cart_product = CartProduct.objects.select_related('product').filter(cart_id=cart_id)
    full_price = total_sum(cart_product)
    if not cart:
        return redirect(reverse('catalog:home'))
    context = {'cart_product': cart_product,
               'full_price': full_price}
    return render(request, 'cart_page.html', context)


def total_sum(cart_product):
    price = 0
    for product in cart_product:
        quantity = cart_product.first().quantity
        price += product.first().product.price*quantity
    return round(price, 2)


def checkout(request):
    cart = Cart.objects.get(user_id=request.user)
    cart_products = CartProduct.objects.select_related('product').filter(cart_id=cart.id)
    customer = Customer.objects.get(user=request.user)
    for cart_product in cart_products:
        cart_product.product.quantity -= cart_product.quantity
        cart_product.save()
        cart_product.product.save()
        order = Order.objects.create(user=customer)
        order.products.add(*cart_products)
        order.save()
    cart.is_active = False
    cart.save()

    return redirect(reverse('catalog:home'))


@login_required(login_url=reverse_lazy('authentication:login'))
def change_quantity(request, product_id):
    cart_product = CartProduct.objects.get(id=product_id)
    quantity_from_html = int(request.POST.get('quantity'))
    if quantity_from_html <= cart_product.product.quantity:
        cart_product.quantity = quantity_from_html
        cart_product.save()
    return redirect(reverse('cart:cart'))
