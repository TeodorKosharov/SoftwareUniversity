from django.shortcuts import render
from django.views.generic import ListView
from pagination.web.models import Products


class DisplayProducts(ListView):
    model = Products
    template_name = 'display-products.html'

    def get(self, request, *args, **kwargs):
        self.request.session['value'] = 5
        print(self.request.session['value'])
        return super().get(request, *args, **kwargs)

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size')
