from django import forms
from django.db import models


# Create your models here.
class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    
class Estudiante(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    
class Profesor(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)
    
class Entregable(models.Model):
    
    nombre=models.CharField(max_length=30)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()

class Usuario(models.Model):
    
    nombre=models.CharField(max_length=30)
    contraseña=models.CharField(max_length=30)
    
class UsuarioFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    contraseña=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=30)