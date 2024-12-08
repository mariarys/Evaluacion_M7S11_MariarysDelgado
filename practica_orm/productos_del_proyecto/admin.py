from django.contrib import admin
from .models import Fabricante, Producto

class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais')  
    search_fields = ('nombre', 'pais')  

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'costo','f_vencimiento', 'fabricante')
    list_filter = ('nombre','fabricante',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
    list_per_page = 2 

    def costo(self, obj):
        if obj. precio < 3000:
            return "Costo Bajo"
        else:
            return "Costo Alto"
      
    
    costo.short_description = 'costo'
    costo.admin_order_field = ' precio' 

admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Producto, ProductoAdmin)
# Register your models here.
