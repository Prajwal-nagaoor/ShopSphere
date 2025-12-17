from django.urls import path
from delivery import views
urlpatterns = [
    path('delivery_form', views.delivery__from,name='delivery_from'),
    path('update_order/<int:pk>/', views.update_order,name='update_order')
]