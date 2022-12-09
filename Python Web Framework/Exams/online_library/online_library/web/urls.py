from django.urls import path
from online_library.web.views import *

urlpatterns = (
    path('', home_page, name='home page'),
    path('add/', add_book_page, name='add book page'),
    path('edit/<int:pk>/', edit_book_page, name='edit book page'),
    path('details/<int:pk>/', book_details_page, name='book details page'),
    path('profile/', profile_page, name='profile page'),
    path('profile/edit/', edit_profile_page, name='edit profile page'),
    path('profile/delete/', delete_profile_page, name='delete profile page'),

    path('register/', register, name='register'),
    path('delbook/<int:pk>/', delete_book, name='delete book')
)
