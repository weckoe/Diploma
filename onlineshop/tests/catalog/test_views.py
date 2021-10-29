from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Product
from tests.catalog.fixtures.products import TEST_ALL_PRODUCTS


class TestSingleProductView(TestCase):

    def test_all_products(self):
        client = Client()
        Product.objects.create(**TEST_ALL_PRODUCTS)
        url = reverse('category:single_product_view', kwargs={'product_slug': TEST_ALL_PRODUCTS['slug']})
        response = client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

