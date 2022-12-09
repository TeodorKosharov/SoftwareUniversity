from django.urls import path
from web_tools_demos.web.views import *

urlpatterns = (
    path('', index, name='index'),
    path('error/', raise_error, name='error'),
    path('employees/', EmployeesListView.as_view(), name='employees list')
)

from .signals import *
