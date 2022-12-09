from django.urls import path, include
from regular_exam.web.views import *

urlpatterns = (
    path('', index_page, name='index page'),

    path('profile/', include([
        path('create/', profile_create_page, name='profile create page'),
        path('details/', profile_details_page, name='profile details page'),
        path('edit/', profile_edit_page, name='profile edit page'),
        path('delete/', profile_delete_page, name='profile delete page')
    ])),

    path('car/', include([
        path('create/', car_create_page, name='car create page'),
        path('<int:pk>/details/', car_details_page, name='car details page'),
        path('<int:pk>/edit/', car_edit_page, name='car edit page'),
        path('<int:pk>/delete/', car_delete_page, name='car delete page')
    ])),

    path('catalogue/', catalogue_page, name='catalogue page')
)
