from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from AppCoder.models import Curso

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()
    profesion = forms.CharField(widget=forms.Textarea)

class InscripcionFormulario(forms.Form):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=True)
    
    nombre = forms.CharField(max_length=30, required=True)
    apellido = forms.CharField(max_length=30, required=True)
    telefono = forms.CharField(max_length=15, required=True)

class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    camada = forms.IntegerField(required=True)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)


class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso. Por favor, elige otro.')
        return email


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen']
