from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, DetailView
from my_auth_tests.web.forms import RegisterForm, AddProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from my_auth_tests.web.models import Product

UserModel = get_user_model()


class ShowUsers(ListView):
    template_name = 'show-users.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        is_logged = user.is_authenticated
        context['logged_user'] = self.request.user if user.__class__.__name__ != 'AnonymousUser' else None
        context['is_logged'] = is_logged
        return context


class ShowProducts(LoginRequiredMixin, ListView):
    # login_url = '/login/' този ред е закоментиран, защото в settings.py вече сме указали кой е адресът за логване
    template_name = 'show-products.html'
    model = Product
    context_object_name = 'products'

    # Променяме върната колекция от обекти от модела Product, като филтрираме обектите, чието поле price има стойност > 100
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(price__gt=100)
        return queryset


class AddProducts(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # login_url = '/login/'
    template_name = 'add-product.html'
    model = Product
    form_class = AddProductForm
    permission_required = ('web.add_product',)
    success_url = '/products/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductDetails(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product-details.html'
    context_object_name = 'selected_product'


# Register/Login/Logout:
class LoginPage(LoginView):
    template_name = 'login-page.html'


class RegisterPage(CreateView):
    template_name = 'register-page.html'
    model = UserModel
    form_class = RegisterForm
    success_url = '/'


class LogoutPage(LogoutView):
    pass
