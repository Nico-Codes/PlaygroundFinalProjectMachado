from django.urls import path
from AppCoder import views
from .views import crear_producto

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    path('crear_producto/', crear_producto, name='crear producto')
]
