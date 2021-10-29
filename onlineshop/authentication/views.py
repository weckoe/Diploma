from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse

from catalog.views import home
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .bl import new_user_add


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('catalog:home'))
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('catalog:home'))
                else:
                    return ValidationError('Disabled account')
            else:
                return ValidationError('Invalid login')
    else:
        login_form = LoginForm()
    return render(request, 'login_page.html', {'login_form': login_form})


def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('catalog:home'))
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user_form = new_user_add(user_form)
            return redirect(reverse('catalog:home'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration_page.html', {'user_form': user_form})


def logout_view(request):
    logout(request)
    return redirect(reverse('catalog:home'))
