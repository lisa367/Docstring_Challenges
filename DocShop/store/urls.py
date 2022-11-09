from django.urls import path
from .views import index, product_detail, add_to_cart, cart, delete_cart, update_quatities, checkout_success, create_checkout_session

app_name = "store"

urlpatterns = [

    path('', index, name="index"),
    path('product/<str:slug>', product_detail, name="product"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
    path('cart/', cart, name="cart"),
    path('cart/update_quatities/', update_quatities, name="update_quatities"),
    path('cart/delete/', delete_cart, name="delete-cart"),
    path('cart/create_checkout_session/', create_checkout_session, name="create_checkout_session"),
    path('cart/success/', checkout_success, name="checkout_success"),

]