DEMO PROYECTO
link del video: https://drive.google.com/file/d/1HdOdBQrxDolcyWohBvWbAKRo0ZcclbQx/view?usp=sharing

Playground Final Project Machado
Este proyecto es una aplicación web desarrollada con Django que gestiona cursos, profesores e inscripciones.

Instalación
Clonar el Repositorio:
(bash) git clone https://github.com/Nico-Codes/PlaygroundFinalProjectMachado.git Navegar al Directorio del Proyecto:

(bash) Copy code cd PlaygroundFinalProjectMachado Instalar Dependencias:

(bash) Copy code pip install -r requirements.txt Aplicar Migraciones:

(bash) Copy code python manage.py migrate Ejecución Iniciar el Servidor de Desarrollo:

(bash) Copy code python manage.py runserver Acceder a la Aplicación:

Visita http://127.0.0.1:8000/ en tu navegador.

Secciones y Funcionalidades Inicio: Presenta una página de inicio.

Cursos: Permite ver una lista de cursos disponibles. Permite crear, editar y eliminar cursos (requiere privilegios de superusuario).

Profesores: Muestra una lista de profesores. Posibilidad de ver detalles, editar y eliminar profesores (requiere privilegios de superusuario).

Inscripciones: Permite a los usuarios inscribirse en cursos disponibles. Solo accesible para usuarios autenticados.

Contribuir Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio. Crea una nueva rama: git checkout -b feature/nueva-funcionalidad. Realiza tus cambios y haz commit: git commit -m 'Añadir nueva funcionalidad'. Haz push a la rama: git push origin feature/nueva-funcionalidad. Crea un pull request en GitHub.
