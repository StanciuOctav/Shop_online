from django.urls import path
from . import views

urlpatterns = [
    # cautam un integer in path si acelasi nume trebuie sa il aiba si variabila din antetul functie
    # daca aici este id1 si noi apelam functia index atunci un antetul functiei trebuie sa fie variabila id1
    path('', views.index, name='index'),
]
