from django.urls import path
from my_tests.web.views import *

urlpatterns = (
    path('form1/', form1, name='form 1'),
    path('form2/', form2, name='form 2'),
    path('check/', check_tasks, name='check tasks'),
    path('count/', count_tasks, name='count tasks'),
    path('students/', students, name='students'),
    path('pets/', pets, name='pets'),
    path('edit/', edit_person, name='edit person'),
    path('widgets/', widgets_demo, name='widgets demo'),
    path('widgets2/', widgets_demo2, name='widgets demo 2'),
    path('media-demo/', mediafiles_demo, name='media demo')
)
