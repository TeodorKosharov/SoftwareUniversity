from django.urls import path, include
from my_music_app.web.views import *

urlpatterns = (
    path('', home, name='home page'),

    path('album/', include([
        path('add/', add_album_page, name='add album page'),
        path('details/<int:pk>/', details_album_page, name='details album page'),
        path('edit/<int:pk>/', edit_album_page, name='edit album page'),
        path('delete/<int:pk>/', delete_album_page, name='delete album page')
    ])),

    path('profile/', include([
        path('register/', register_page, name='register user'),
        path('logged-in/', logged_in, name='logged in'),
        path('details/', profile_details_page, name='profile details page'),
        path('delete/', profile_delete_page, name='profile delete page')
    ]))
)
