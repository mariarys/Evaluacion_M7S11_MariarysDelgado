from django.urls import path
from . import views


urlpatterns = [
    path('producto/', views.lista_productos, name ='lista_productos'),
    path('agregar/',views.agregar_productos,name = 'agregar_productos'),
    path('producto/<int:pk>/', views.mostrar_producto, name='mostrar_producto'),
    path('crearusuario/',views.ingresar_usuario, name = 'crearusuario'),
    

]
