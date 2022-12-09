from django.urls import path
from django.views.generic import RedirectView
from cbv.web.views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('template/', IndexViewWithListView.as_view()),
    path('redirect-to-index/', RedirectView.as_view(url='/')),
    path('details/<int:pk>/', EmployeeDetailsView.as_view(), name='employee details'),
    path('create/', EmployeeCreateView.as_view(), name='employee create'),
    path('update/<int:pk>/', UpdateView.as_view(), name='employee update')

]
