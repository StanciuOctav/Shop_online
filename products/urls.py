from django.urls import path
from . import views

urlpatterns = [
    # cautam un integer in path si acelasi nume trebuie sa il aiba si variabila din antetul functie
    # daca aici este id1 si noi apelam functia index atunci un antetul functiei trebuie sa fie variabila id1

    # path uri pentru clienti
    path('show/', views.list_products, name='list_products'),
    path('show/<str:p_name>/', views.detailed_product, name='detailed_product'),

    # path uri pentru admin
    path('createProduct/', views.create_product, name='create_product'),
    path('delete/<str:p_name>/', views.delete_product, name='delete_product'),
    path('update/<str:p_name>/', views.update_product, name='update_product'),
    path('renameClient/', views.renameClient, name='renameClient'),

    #ptr rename
    path('rename/<str:username>/', views.rename, name='rename'),

]
