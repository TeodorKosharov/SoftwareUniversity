from django.urls import path
from django_rest_framework.api.views import *

urlpatterns = (
    path('books/', ListBooksView.as_view(), name="books-all"),
    path('get/', get_data),
    path('post/', add_item),
    path('get-items/', get_items, name='get items'),
    path('demo/', demo_view)
)
