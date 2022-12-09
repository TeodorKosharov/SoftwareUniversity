from django.urls import path
from user_test.web.views import *

urlpatterns = (
    path('reg/', Registration.as_view(), name='reg view'),
)
