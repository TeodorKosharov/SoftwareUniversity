from django.urls import path
from notes_app.web.views import *

urlpatterns = (
    path('', home_page, name='home page'),
    path('add/', add_note_page, name='add note page'),
    path('edit/<int:pk>/', edit_note_page, name='edit note page'),
    path('delete/<int:pk>/', delete_note_page, name='delete note page'),
    path('details/<int:pk>/', note_details_page, name='note details page'),
    path('profile/', profile_page, name='profile page'),

    path('register/', register_page, name='register page'),
    path('delete/', delete, name='delete profile')
)
