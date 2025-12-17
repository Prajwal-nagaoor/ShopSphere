from django.urls import path
from . import views
urlpatterns = [
    path('home', views.hoem, name='home'),
    path('add_product', views.add_product, name='add_product'),
    path('add_cart/<int:pk>/', views.add_cart, name='add_cart'),
    path('cart', views.cart, name='cart'),
]