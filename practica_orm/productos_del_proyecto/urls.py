from django.urls import path
from . import views

urlpatterns = [
    path('producto/', views.lista_productos, name ='lista_productos'),
    path('agregar/',views.agregar_productos,name = 'agregar_productos'),
    path('producto/username/<str:cadena>/', views.mostrar_cadena, name='mostrar_cadena'),

]
