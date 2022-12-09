from django.urls import path, include
from gamesplay_app.web.views import *

urlpatterns = (
    path('', home_page, name='home page'),

    path('profile/', include([
        path('create/', create_profile_page, name='create profile page'),
        path('details/', profile_details_page, name='profile details page'),
        path('edit/', edit_profile_page, name='edit profile page'),
        path('delete/', delete_profile_page, name='delete profile page')
    ])),

    path('game/', include([
        path('create/', create_game_page, name='create game page'),
        path('details/<int:pk>/', details_game_page, name='details game page'),
        path('edit/<int:pk>/', edit_game_page, name='edit game page'),
        path('delete/<int:pk>/', delete_game_page, name='delete game page'),
    ])),

    path('dashboard/', dashboard_page, name='dashboard page')
)
