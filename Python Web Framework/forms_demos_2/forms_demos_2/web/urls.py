from django.urls import path

from forms_demos_2.web.views import index, index_2, index_3

urlpatterns = (
    path('', index, name='index'),
    path('idx2/', index_2, name='index 2'),
    path('idx3/', index_3, name='index 3')
)
