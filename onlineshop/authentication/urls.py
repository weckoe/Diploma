from django.urls import path
from authentication.views import login_view, registration, logout_view

app_name = 'authentication'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout_view, name='logout')
]
