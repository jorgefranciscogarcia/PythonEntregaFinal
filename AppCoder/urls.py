from django.urls import path

from AppCoder import views
from AppCoder.models import Curso

#Estas son las URLS a las que puedo ingresar en el navegador
urlpatterns = [
    path('', views.inicio),
    path('cursos', views.cursos, name="Cursos"),
    path('formulario', views.formulario, name="Formulario"),
    path('leerUsuarios', views.leerUsuarios, name="LeerUsuarios"),
]
