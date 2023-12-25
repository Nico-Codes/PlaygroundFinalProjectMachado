from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegistroTestCase(TestCase):
    def test_registro_exitoso(self):
        # Simular un formulario de registro válido
        datos_registro = {
            'username': 'nuevo_usuario',
            'password1': 'contrasenia123',
            'password2': 'contrasenia123',
        }

        # Enviar solicitud POST al endpoint de registro
        response = self.client.post(reverse('registro'), data=datos_registro)

        # Verificar redirección a la página de inicio
        self.assertRedirects(response, reverse('inicio'))

        # Verificar que el usuario fue creado en la base de datos
        self.assertTrue(User.objects.filter(username='nuevo_usuario').exists())
