from django.contrib import admin
from .models import Fabricante,Producto

class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais') 
    search_fields = ('nombre', 'pais') 

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'fabricante')
    list_filter = ('fabricante',)  
    search_fields = ('nombre', 'descripcion') 
    ordering = ('fabricante', 'nombre')  

admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Producto,ProductoAdmin)
# Register your models here.
