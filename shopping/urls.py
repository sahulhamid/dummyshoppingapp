from django.urls import path
from .views import *


urlpatterns = [
    path('',home.as_view(),name='home'),
    path('add',add.as_view(),name='add'),
    path('viewproduct_electronics',viewproduct_electronics,
    name='viewproduct_electronics'),
    path('viewproduct_furniture',viewproduct_furniture,
    name='viewproduct_furniture'),
    path('addcart/<str:pk>/',add_to_cart,name='addcart'),
    path('removecart/<str:pk>/',remove_from_cart,name='removecart'),
    path('mycart',viewcart,name='mycart'),
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('profile',profile,name='profile'),
    path('buy/<str:pk>/',buy,name='buy')
]