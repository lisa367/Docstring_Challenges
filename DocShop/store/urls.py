from django.urls import path
from .views import index, product_detail, add_to_cart, cart, delete_cart


urlpatterns = [

    path('', index, name="index"),
    path('product/<str:slug>', product_detail, name="product"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
    path('cart/', cart, name="cart"),
    path('cart/delete/', delete_cart, name="delete-cart"),

]