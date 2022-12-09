from django.urls import path
from my_auth_tests.web.views import *

urlpatterns = (
    path('', ShowUsers.as_view(), name='show users'),
    path('login/', LoginPage.as_view(), name='login page'),
    path('register/', RegisterPage.as_view(), name='register page'),
    path('logout/', LogoutPage.as_view(), name='logout page'),
    path('products/', ShowProducts.as_view(), name='show products'),
    path('add-product/', AddProducts.as_view(), name='add product'),
    path('details/product/<int:pk>/', ProductDetails.as_view(), name='details product')
)
