from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from authentication.models import User
from cart.models import Cart, CartProduct
from catalog.models import Product, Category
from tests.catalog.fixtures.products import TEST_ALL_PRODUCTS
from tests.catalog.fixtures.categories import TEST_ALL_CATEGORIES
from tests.catalog.fixtures.user import TEST_USER


class TestSingleProductView(TestCase):
    def test_single_product_view(self):
        client = Client()
        user = User(
            username="admin"
        )
        user.set_password("123")
        user.save()
        client.login(username=user.username, password="123")
        category = Category.objects.create(**TEST_ALL_CATEGORIES)
        product = Product.objects.create(**TEST_ALL_PRODUCTS, category=category)
        cart = Cart.objects.create(user_id=user.id, active=True)
        cartproduct = CartProduct.objects.create(product=product, cart=cart, quantity=2)
        url = reverse('catalog:single_product_view', kwargs={'product_slug': TEST_ALL_PRODUCTS['slug']})
        response = client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.templates[0].name, 'single_product.html')
        self.assertEqual(response.context['single_product'].slug, TEST_ALL_PRODUCTS['slug'])
        self.assertEqual(response.context['single_product'].name, TEST_ALL_PRODUCTS['name'])
        self.assertEqual(response.context['is_in_cart'], True)


class TestCategoriesView(TestCase):
    def test_categories_view(self):
        client = Client()
        category = Category.objects.create(**TEST_ALL_CATEGORIES)
        url = reverse('catalog:categories_view', kwargs={'category_slug': TEST_ALL_CATEGORIES['slug']})

        response = client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.templates[0].name, 'single_category.html')
        self.assertEqual(response.context['single_category'].name, TEST_ALL_CATEGORIES['name'])
