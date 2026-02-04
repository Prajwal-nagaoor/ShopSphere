from django.urls import path
from . import views
urlpatterns = [
    path('home', views.hoem, name='home'),
    path('add_product', views.add_product, name='add_product'),
    path('add_cart/<int:pk>/', views.add_cart, name='add_cart'),
    path('cart', views.cart, name='cart'),
    path('cartcount/<int:pk>/', views.cart_increase, name='cart_increase'),
    path('cartdescrease/<int:pk>/', views.cart_decrease, name='cart_decrease'),
    path('cartprodel/<int:pk>/', views.cart_pro_remove, name='cart_pro_remove'),
    path('pro_details/<int:pk>/', views.pro_details, name='pro_details'),
]