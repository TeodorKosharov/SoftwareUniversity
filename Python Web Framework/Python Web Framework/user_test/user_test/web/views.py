from django.shortcuts import render
from django.views.generic import CreateView
from user_test.web.models import AppUser
from user_test.web.forms import RegForm


class Registration(CreateView):
    template_name = 'register.html'
    model = AppUser
    form_class = RegForm
    success_url = '/admin/'
