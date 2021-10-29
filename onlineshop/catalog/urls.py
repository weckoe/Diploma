
from django.urls import path
from catalog.views import home, categories_view, single_product_view


app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:category_slug>/', categories_view, name='categories_view'),
    path('product/<slug:product_slug>/', single_product_view, name='single_product_view'),
]
