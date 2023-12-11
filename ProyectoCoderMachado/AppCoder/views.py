from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

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