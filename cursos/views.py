from django.shortcuts import render
from .forms import ComentarioContactoForm
from .models import ComentarioContacto, Cursos
from django.shortcuts import get_object_or_404
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages 

def registros(request):
    cursos=Cursos.objects.all()
    return render(request, "registros/cursos.html", {"cursos":cursos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save() #inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})

    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})

def eliminarComentarioContacto(request, id,
    confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados.

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
    #Si el formulario no es valido nos regresa al formulario para verificar
    #datos
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})

def contacto(request):
    comentario = ComentarioContacto.objects.all()
    return render(request,'registros/contacto.html',{'comentario':comentario})

def consultaContacto(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request,'registros/consultaContacto.html',{'comentarios':comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo =request.POST['titulo']
            descripcion =request.POST['descripcion']
            archivo =request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, 'registros/archivos.html')
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'registros/archivos.html', {'archivo':Archivos})
    
def consultasSQL(request):
    alumnos=Archivos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos where carrera="TI" ORDER BY turno DESC')
    return render (request, 'registros/consultas.html', {'alumnos':alumnos})