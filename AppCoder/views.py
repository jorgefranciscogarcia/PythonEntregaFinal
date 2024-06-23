from django.shortcuts import HttpResponse, render

from AppCoder.models import Curso, Usuario


# Create your views here.
def curso(self):
    
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"Curso: {curso.nombre} Camada: {curso.camada}"
    
    return HttpResponse(documentoDeTexto)

def inicio(request):
    
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def formulario(request):
    
    if request.method == 'POST':
        
        nombre = nombre ( request.POST['nombre'], request.POST['contraseña'])
        
        nombre.save()
        
        return render(request, "AppCoder/inicio.html")
    
    return render(request, "AppCoder/formulario.html")

def __str__(self):
    return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email}"

def leerUsuarios(request):
    
    usuarios = Usuario.objects.all()
    contexto = {"usuarios": usuarios}
    
    return render(request, "AppCoder/leerUsuarios.html", contexto)