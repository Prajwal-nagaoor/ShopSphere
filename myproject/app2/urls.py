from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_, name='logout'),
    path('update', views.update, name='update'),
]