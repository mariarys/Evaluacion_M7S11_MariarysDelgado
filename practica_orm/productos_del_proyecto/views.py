from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm


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

def mostrar_producto(request, pk):
    try:
        producto = Producto.objects.get(pk = pk)
    except Producto.DoesNotExist:
        return HttpResponse("Producto no encontrado", status=404)

    context = {
        'producto': producto,
    }
    return render(request, 'supermercado/detalle_producto.html', context)

def ingresar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡El usuario se ha registrado exitosamente!")
            return redirect('ingresr_usuario')  # Asegúrate de tener una vista 'login' configurada
    else:
        form = CustomUserCreationForm()
    return render(request, 'supermercado/ingresar_usuario.html', {'form': form})

