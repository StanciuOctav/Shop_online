from django.urls import path
from . import views

urlpatterns = [
    # path uri pentru clienti
    path('', views.show_cart, name='show_cart'),
]
