from django.shortcuts import render,redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request,'supermercado/lista_productos.html',{'productos': productos})


def agregar_productos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        f_vencimiento = request.POST.get('fecha_vencimiento')
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            f_vencimiento=f_vencimiento
        )
        return redirect('lista_productos')
    return render(request, 'supermercado/agregar_producto.html')



