from django.contrib import admin
from .models import Curso,Profesor,Inscripcion,Avatar

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Inscripcion)
admin.site.register(Avatar)