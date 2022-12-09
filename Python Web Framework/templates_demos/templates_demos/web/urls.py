from django.urls import path
from templates_demos.web.views import base, index

urlpatterns = (
    path('', base, name='default page'),
    path('index/', index, name='index')
)
