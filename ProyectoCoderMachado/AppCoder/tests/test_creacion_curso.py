from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from models import Curso

class CrearCursoTestCase(TestCase):
    def setUp(self):
        # Crear un superusuario para las pruebas
        self.superusuario = User.objects.create_superuser(username='admin', password='admin123', email='admin@example.com')

    def test_creacion_curso(self):
        # Iniciar sesión como superusuario
        self.client.login(username='admin', password='admin123')

        # Simular un formulario de creación de curso válido
        datos_curso = {
            'nombre': 'Nuevo Curso',
            'camada': '2023',
            'descripcion': 'Descripción del nuevo curso.',
        }

        # Enviar solicitud POST al endpoint de creación de curso
        response = self.client.post(reverse('crear_curso'), data=datos_curso)

        # Verificar redirección a la lista de cursos
        self.assertRedirects(response, reverse('lista_cursos'))

        # Verificar que el nuevo curso fue creado en la base de datos
        self.assertTrue(Curso.objects.filter(nombre='Nuevo Curso').exists())
