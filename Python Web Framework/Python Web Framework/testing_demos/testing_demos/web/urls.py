from django.urls import path
from testing_demos.web.views import *

urlpatterns = (
    path('', ProfilesListView.as_view(), name='list profiles'),
    path('create/', ProfileCreateView.as_view(), name='create profile')
)
