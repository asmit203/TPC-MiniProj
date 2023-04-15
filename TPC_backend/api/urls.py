from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('user/', views.get_user),
    path('logout/', views.logout),
    path('profile/', views.get_profile),
    path('applied/', views.get_applied),
]