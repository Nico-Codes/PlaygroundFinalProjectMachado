from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    
    path('inscripcion/', views.inscripcion, name="inscripcion"),
    

   
    path('profesores/', views.ProfesorListView.as_view(), name='ListaProfesores'),
    path('profesores/<int:pk>/', views.ProfesorDetailView.as_view(), name='DetalleProfesor'),
    path('profesores/crear/', views.ProfesorCreateView.as_view(), name='CrearProfesor'),
    path('profesores/editar/<int:pk>/', views.ProfesorUpdateView.as_view(), name='EditarProfesor'),
    path('profesores/borrar/<int:pk>/', views.ProfesorDeleteView.as_view(), name='BorrarProfesor'),
    path('profesores/inscribirse/<int:profesor_id>/', views.inscribirse_en_profesor, name='InscribirseProfesor'),

   
    path('cursos/lista', views.CursoListView.as_view(), name = "ListaCursos"),
    path('cursos/nuevo', views.CursoCreateView.as_view(), name = "NuevoCurso"),
    path('cursos/<pk>', views.CursoDetailView.as_view(), name = "DetalleCurso"),
    path('cursos/<pk>/editar', views.CursoUpdateView.as_view(), name = "EditarCurso"),
    path('cursos/<pk>/borrar', views.CursoDeleteView.as_view(), name = "BorrarCurso"),
  
  
    path('login', views.login_request, name="Login"),
    path('registro', views.registro, name="Registro"),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='Logout'),

    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('cambiarContrasenia', views.CambiarContrasenia.as_view(), name="CambiarContrasenia"),


]   

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
