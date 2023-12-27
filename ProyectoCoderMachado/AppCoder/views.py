from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseForbidden
from .forms import ProfesorFormulario, CursoFormulario, InscripcionFormulario, UserCreationFormCustom, UserEditForm
from .models import Curso, Inscripcion, Profesor, Avatar
from django.shortcuts import render
from AppCoder import forms
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView



def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def es_superusuario(user):
    return user.is_superuser


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
        inscripciones = Inscripcion.objects.all()  # Recuperar todas las inscripciones
        return render(request, 'AppCoder/inscripcion.html', {"form": nuevo_inscripto, "inscripciones": inscripciones})
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
    context_object_name = "profesores"
    template_name = "AppCoder/profesores_lista.html"

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = "AppCoder/profesor_detalle.html"

@method_decorator(user_passes_test(es_superusuario), name='dispatch')
class ProfesorCreateView(SuperusuarioMixin, CreateView):
    model = Profesor
    template_name = "AppCoder/profesor_crear.html"
    success_url = reverse_lazy('ListaProfesores')
    fields = ['nombre', 'apellido','profesion']

@method_decorator(user_passes_test(es_superusuario), name='dispatch')
class ProfesorUpdateView(SuperusuarioMixin, UpdateView):
    model = Profesor
    template_name = "AppCoder/profesor_editar.html"
    success_url = reverse_lazy('ListaProfesores')
    fields = ['nombre', 'apellido','profesion']

@method_decorator(user_passes_test(es_superusuario), name='dispatch')
class ProfesorDeleteView(SuperusuarioMixin, DeleteView):
    model = Profesor
    template_name = "AppCoder/profesor_borrar.html"
    success_url = reverse_lazy('ListaProfesores')

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

def sobremi_view(request):
    return render(request, 'AppCoder/sobremi.html')

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
            user = form.save()

            login(request, user)

            return render(request, 'AppCoder/inicio.html', {'user': user})

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

@login_required
def cambiar_contrasenia(request):
    if request.method == 'POST':
        form_contrasenia = PasswordChangeForm(user=request.user, data=request.POST)
        if form_contrasenia.is_valid():
            usuario = form_contrasenia.save()
            update_session_auth_hash(request, usuario)
            return render(request, "AppCoder/contrasenia_cambiada.html")

    else:
        form_contrasenia = PasswordChangeForm(user=request.user)

    return render(request, 'AppCoder/cambiar_contrasenia.html', {'form_contrasenia': form_contrasenia})

def Logout(request):
    logout(request)
    return render(request, "AppCoder/inicio.html")

def contrasenia_cambiada(request):
    return render(request, 'AppCoder/contrasenia_cambiada.html')