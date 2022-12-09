from django.urls import path
from users_demos.web.views import *

urlpatterns = (
    path('', UsersListView.as_view(), name='index'),
)
