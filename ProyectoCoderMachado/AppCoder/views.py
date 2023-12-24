from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordChangeView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.http import HttpResponseForbidden
from .forms import ProfesorForm, CursoFormulario, InscripcionFormulario, UserCreationFormCustom, UserEditForm, InscripcionForm
from .models import Curso, Inscripcion, Profesor, Avatar
from django.shortcuts import render, get_object_or_404, redirect
from .forms import InscripcionForm
from AppCoder import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def es_superusuario(user):
    return user.is_superuser

@user_passes_test(es_superusuario)
def cursos(request):
    if request.method == "POST":
        nuevo_formulario = CursoFormulario(request.POST)
        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nuevo_curso = Curso(
                nombre=informacion["nombre"],
                camada=informacion["camada"],
                descripcion=informacion["descripcion"],
            )
            nuevo_curso.save()
            return render(request, 'AppCoder/inicio.html')

    nuevo_formulario = CursoFormulario()
    return render(request, 'AppCoder/cursos.html', {"formulario": nuevo_formulario})

@user_passes_test(es_superusuario)
def profesores(request):
    usuario_id = request.user.id

    # Verificar si el profesor ya existe
    if Profesor.objects.filter(usuario__id=usuario_id).exists():

        # Puedes redirigir o mostrar un mensaje indicando que el profesor ya existe
        return render(request, 'AppCoder/profesores.html')

    if request.method == "POST":
        nuevo_profesor = ProfesorForm(request.POST)
        if nuevo_profesor.is_valid():
            # No necesitas crear un nuevo formulario, puedes acceder a los datos directamente
            informacion = nuevo_profesor.cleaned_data
            nuevo_profesor = Profesor(
                usuario_id=usuario_id,
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                profesion=informacion["profesion"]
            )
            nuevo_profesor.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        nuevo_profesor = ProfesorForm()

    return render(request, 'AppCoder/profesores.html', {"formulario": nuevo_profesor})

def inscripcion(request):
    if request.method == "POST":
        nuevo_inscripto = InscripcionFormulario(request.POST)
        if nuevo_inscripto.is_valid():
            informacion = nuevo_inscripto.cleaned_data
            Inscripcion.objects.create(
                curso=informacion["curso"],
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                telefono=informacion["telefono"],
            )
            return render(request, 'AppCoder/mensaje_inscripcion.html')
    else:
        nuevo_inscripto = InscripcionFormulario()
        return render(request, 'AppCoder/inscripcion.html', {"inscripcion": nuevo_inscripto})

def es_superusuario(user):
    return user.is_superuser

def es_superusuario(user):
    return user.is_superuser

class SuperusuarioMixin:
    @method_decorator(user_passes_test(es_superusuario, login_url=None))
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden("Acceso denegado")
        return super().dispatch(*args, **kwargs)

class ProfesorListView(ListView):
    model = Profesor
    context_object_name = 'profesores'
    template_name = 'AppCoder/profesores_lista.html'

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'AppCoder/profesor_detalle.html'

@method_decorator(user_passes_test(es_superusuario), name='dispatch')
class ProfesorCreateView(SuperusuarioMixin, CreateView):
    model = Profesor
    form_class = ProfesorForm  # Cambiado a ProfesorForm
    template_name = 'AppCoder/profesor_form.html'
    success_url = 'AppCoder/inicio.html'

@method_decorator(user_passes_test(es_superusuario), name='dispatch')
class ProfesorUpdateView(SuperusuarioMixin, UpdateView):
    model = Profesor
    template_name = 'AppCoder/profesor_editar.html'
    form_class = forms.ProfesorForm
    success_url = reverse_lazy('ListaProfesores')

@method_decorator(user_passes_test(es_superusuario), name='dispatch')
class ProfesorDeleteView(SuperusuarioMixin, DeleteView):
    model = Profesor
    template_name = 'AppCoder/profesor_borrar.html'
    success_url = reverse_lazy('ListaProfesores')

def inscribirse_en_profesor(request, profesor_id):
    if request.method == 'POST':
        # Lógica para inscribirse en un profesor
        pass
    return render(request, 'AppCoder/inicio.html', {'profesor_id': profesor_id})

class SuperusuarioMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class CursoListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "AppCoder/cursos_lista.html"

class CursoDetailView(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

@method_decorator(user_passes_test(es_superusuario), name='dispatch')
class CursoCreateView(SuperusuarioMixin, CreateView):
    model = Curso
    template_name = "AppCoder/curso_crear.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre', 'camada','descripcion']

@method_decorator(user_passes_test(es_superusuario), name='dispatch')
class CursoUpdateView(SuperusuarioMixin, UpdateView):
    model = Curso
    template_name = "AppCoder/curso_editar.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre', 'camada','descripcion']

@method_decorator(user_passes_test(es_superusuario), name='dispatch')
class CursoDeleteView(SuperusuarioMixin, DeleteView):
    model = Curso
    template_name = "AppCoder/curso_borrar.html"
    success_url = reverse_lazy('ListaCursos')

def inscribirse_en_curso(request, curso_id):
    if request.method == 'POST':
        formulario = InscripcionForm(request.POST)
        if formulario.is_valid():
            curso = Curso.objects.get(id=formulario.cleaned_data['curso_id'])
            usuario = request.user
            if not Inscripcion.objects.filter(usuario=usuario, curso=curso).exists():
                Inscripcion.objects.create(usuario=usuario, curso=curso)
    return render(request, "AppCoder/inicio.html", {"curso_id": curso_id})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user:
                login(request, user)
                return render(request, "AppCoder/inicio.html", {"mensaje": f'Bienvenido {user.username}'})
    else:
        form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {"form": form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Usuario Creado"})
    else:
        form = UserCreationFormCustom()
    return render(request, "AppCoder/registro.html", {"form": form})

def editarPerfil(request):
    usuario = request.user

    try:
        avatar_imagen = usuario.avatar.imagen
    except ObjectDoesNotExist:
        avatar_imagen = None

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if hasattr(usuario, 'avatar'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    Avatar.objects.create(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
            miFormulario.save()
            return render(request, "AppCoder/usuario_cambios.html")
    else:
        miFormulario = UserEditForm(instance=usuario)
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "avatar_imagen": avatar_imagen})

def Logout(request):
    logout(request)
    return render(request, "AppCoder/inicio.html")

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'AppCoder/cambiar_contrasenia.html'
    success_url = reverse_lazy('EditarPerfil')