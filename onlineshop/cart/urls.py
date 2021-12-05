from .views import add_to_cart, cart, checkout, change_quantity
from django.urls import path


app_name = 'cart'
urlpatterns = [
    path('', cart, name='cart'),
    path('add-to-cart/<str:slug>/', add_to_cart, name='add-to-cart'),
    path('checkout/', checkout, name='checkout'),
    path('change_quantity/<int:product_id>/', change_quantity, name='change_quantity'),
]
