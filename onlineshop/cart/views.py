from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

from cart.models import Cart, CartProduct, Order, Customer
from catalog.models import Product


@login_required
def add_to_cart(request, slug):
    user = request.user
    product = Product.objects.get(slug=slug)
    new_cart, _ = Cart.objects.get_or_create(user=request.user)
    new_product, _ = CartProduct.objects.get_or_create(product=product, cart=new_cart)
    customer, _ = Customer.objects.get_or_create(user=user)
    return redirect(reverse('catalog:home'))


@login_required
def cart(request):
    user = request.user
    customer, _ = Customer.objects.get_or_create(user=user)
    cart_id = Cart.objects.filter(user_id=user.id, active=True).first()
    if not cart_id:
        return HttpResponseNotFound('<h1> Cart is empty</h1>')
    cart_products = CartProduct.objects.select_related('product').filter(cart_id=cart_id)
    full_price = total_sum(cart_products)
    context = {'cart_product': cart_products,
               'full_price': full_price}
    return render(request, 'cart_page.html', context)


def total_sum(cart_products):
    price = 0
    for product in cart_products:
        quantity = product.quantity
        price += product.product.price * quantity
    return round(price, 2)


@login_required
def checkout(request):
    cart = Cart.objects.get(user_id=request.user)
    if not cart:
        return HttpResponseNotFound('<h1>Cart not found</h1>')
    cart_products = CartProduct.objects.select_related('product').filter(cart_id=cart.id)
    customer = Customer.objects.get(user=request.user)
    order = Order.objects.create(user=customer)
    for cart_product in cart_products:
        cart_product.product.quantity -= cart_product.quantity
        cart_product.save()
        cart_product.product.save()
        order.products.add(*cart_products)
        order.save()
    cart.active = False
    cart.save()

    return redirect(reverse('catalog:home'))


@login_required
def change_quantity(request, product_id):
    cart_product = CartProduct.objects.get(id=product_id)
    quantity_from_html = int(request.POST.get('quantity'))
    if quantity_from_html >= cart_product.product.quantity:
        cart_product.quantity = quantity_from_html
        cart_product.save()
    return redirect(reverse('cart:cart'))
