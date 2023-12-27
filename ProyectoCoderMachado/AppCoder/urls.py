from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name="inicio"),
   
    
    path('inscripcion/', views.inscripcion, name="inscripcion"),
    

   
    path('profesores/lista', views.ProfesorListView.as_view(), name = "ListaProfesores"),
    path('profesores/nuevo', views.ProfesorCreateView.as_view(), name = "NuevoProfesor"),
    path('profesores/<pk>', views.ProfesorDetailView.as_view(), name = "DetalleProfesor"),
    path('profesores/<pk>/editar', views.ProfesorUpdateView.as_view(), name = "EditarProfesor"),
    path('profesores/<pk>/borrar', views.ProfesorDeleteView.as_view(), name = "BorrarProfesor"),

   
    path('cursos/lista', views.CursoListView.as_view(), name = "ListaCursos"),
    path('cursos/nuevo', views.CursoCreateView.as_view(), name = "NuevoCurso"),
    path('cursos/<pk>', views.CursoDetailView.as_view(), name = "DetalleCurso"),
    path('cursos/<pk>/editar', views.CursoUpdateView.as_view(), name = "EditarCurso"),
    path('cursos/<pk>/borrar', views.CursoDeleteView.as_view(), name = "BorrarCurso"),
  
  
    path('login', views.login_request, name="Login"),
    path('registro', views.registro, name="Registro"),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='Logout'),

    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('cambiar_contrasenia/', views.cambiar_contrasenia, name='cambiar_contrasenia'),
    path('contrasenia_cambiada/', views.contrasenia_cambiada, name='contraseña_cambiada'),

    path('sobremi/', views.sobremi_view, name='sobremi'),
]   

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
