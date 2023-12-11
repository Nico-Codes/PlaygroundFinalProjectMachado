from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiante, Producto, Profesor
from .forms import EstudianteFormulario, ProfesorFormulario

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    
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
         



    return render(request, 'AppCoder/cursos.html')


def profesores(request):
     if request.method == "POST":
        nuevo_profesor = ProfesorFormulario(request.POST)

        if nuevo_profesor.is_valid():
            informacion = nuevo_profesor.cleaned_data
            nuevo_profesor = Profesor(
                    nombre = informacion["nombre"],
                    apellido = informacion["apellido"],
                    email = informacion["email"],
                    profesion = informacion["profesion"]
                    )
            nuevo_profesor.save()
            return render(request, 'AppCoder/inicio.html')
     else:
        nuevo_formulario = ProfesorFormulario()
        return render(request, 'AppCoder/profesores.html', {"formulario": nuevo_formulario})
    


# def estudiantes(request):
#        if request.method == "POST":
#         nuevo_estudiante = EstudianteFormulario(request.POST)

#         if nuevo_estudiante.is_valid():
#             informacion = nuevo_estudiante.cleaned_data
#             nuevo_estudiante = Estudiante(
#                     nombre = informacion["nombre"],
#                     apellido = informacion["apellido"],
#                     telefono = informacion["telefono"],
#                     )
#             nuevo_estudiante.save()
#             return render(request, 'AppCoder/inicio.html')
#         else:
#           nuevo_formulario = EstudianteFormulario()          
#           return render(request, 'AppCoder/estudiantes.html', {"formulario": nuevo_formulario})


def estudiantes(request):
    if request.method == "POST":
        nuevo_estudiante = EstudianteFormulario(request.POST)

        if nuevo_estudiante.is_valid():
            informacion = nuevo_estudiante.cleaned_data
            nuevo_estudiante = Estudiante(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                telefono=informacion["telefono"],
            )
            nuevo_estudiante.save()
            return render(request, 'AppCoder/inicio.html')

    # Si llegamos a este punto, o bien es una solicitud GET o una solicitud POST no válida
    nuevo_formulario = EstudianteFormulario()
    return render(request, 'AppCoder/estudiantes.html', {"formulario": nuevo_formulario})
    
def entregables(request):
    return render(request, 'AppCoder/entregables.html')



