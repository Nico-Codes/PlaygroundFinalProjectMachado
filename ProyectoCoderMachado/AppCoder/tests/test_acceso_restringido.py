from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccesoRestringidoTestCase(TestCase):
    def setUp(self):
        # Crear un usuario para las pruebas
        self.usuario = User.objects.create_user(username='usuario_prueba', password='contrasenia123')

    def test_acceso_paginas_restringidas(self):
        # Intentar acceder a la página de edición de perfil sin autenticarse
        response = self.client.get(reverse('editar_perfil'))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('editar_perfil'))

        # Iniciar sesión con el usuario de prueba
        self.client.login(username='usuario_prueba', password='contrasenia123')

        # Intentar acceder a la página de edición de perfil después de iniciar sesión
        response = self.client.get(reverse('editar_perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Editar Perfil')
