from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('logout/', views.logoutPage, name='logoutPage'),
    path('register/', views.registerPage, name='registerPage'),
]