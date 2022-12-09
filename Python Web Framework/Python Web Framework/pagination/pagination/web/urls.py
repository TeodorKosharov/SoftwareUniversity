from django.urls import path
from pagination.web.views import *

urlpatterns = (
    path('', DisplayProducts.as_view(), name='display products'),
)
