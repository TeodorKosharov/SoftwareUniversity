from django.urls import path
from docker_and_deployment.web.views import *

urlpatterns = (
    path('', home_view),
)
