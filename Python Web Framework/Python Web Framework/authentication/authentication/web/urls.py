from django.urls import path

from authentication.web.views import *

urlpatterns = (
    path('', index, name='index'),
    path('login/', create_user_and_login, name='create and login user'),
    path('perms/', check_perms, name='perms user'),
    path('profile/1/', show_profile, name='show profile 1'),
    path('profile/2/', ProfileView.as_view(), name='show profile 2'),

)
