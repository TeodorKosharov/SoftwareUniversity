import random

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from web_tools_demos.web.models import *
from django.views.generic import ListView


def very_slow_operation():
    return random.randint(1, 1024)


@cache_page(1 * 60)  # 60 seconds
def index(request):
    Employees.objects.create(
        first_name='Teodor',
        last_name='Plamenov',
        age='21'
    )

    value = very_slow_operation()

    # Ако нямаме такъв ключ в сесията, върнатият резултат е вторият аргумент - []
    latest_values = request.session.get('LATEST_VALUES_SESSION_KEY', [])
    request.session['LATEST_VALUES_SESSION_KEY'] = latest_values
    return HttpResponse(f'Value is: {value}')


def raise_error(request):
    get_user_model().objects.get(pk=101021)


class EmployeesListView(ListView):
    model = Employees
    template_name = 'employees-list.html'

    # paginate_by = 4

    def get_paginate_by(self, queryset):
        print(self.request.GET)
        return self.request.GET.get('page_size', self.default_paginate_by)
