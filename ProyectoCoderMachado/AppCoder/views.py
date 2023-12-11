from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Insumo
from .forms import InsumoFormulario

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def crear_producto(request):

    print("Mostrar request.post:")
    print(request.POST)

    if request.method == "POST":
        nuevo_producto = Producto(

                nombre = request.POST["nombre"],
                descripcion = request.POST["descripcion"],
                cantidad_en_stock = request.POST["cantidad_en_stock"]

         )
        nuevo_producto.save()
        return render(request, "AppCoder/inicio.html")
    
    print("Mostrar request.post:")
    print(request.POST)
         



    return render(request, 'AppCoder/producto_formulario.html')

def crear_insumo(request):

    if request.method == "POST":
        nuevo_formulario = InsumoFormulario(request.POST)

        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nuevo_insumo = Insumo(
                    nombre = informacion["nombre"],
                    descripcion = informacion["descripcion"],
                    unidad_de_medida = informacion["unidad_de_medida"],
                    cantidad_en_stock = informacion["cantidad_en_stock"]
                    )
            nuevo_insumo.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        nuevo_formulario = InsumoFormulario()
        return render(request, 'AppCoder/insumo_formulario.html', {"formulario": nuevo_formulario})
    
