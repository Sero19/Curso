from django.db import models
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextField



class Cursos(models.Model): #Define la estructura de la tabla
    
    NombreCurso = models.CharField(max_length=100, verbose_name="Curso") #Define el tipo de dato y el tamaño
    Descripcion = models.TextField() 
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Imagen del Curso")
    created = models.DateTimeField(auto_now_add=True) #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True) #Fecha de actualizacion
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
    def __str__(self):
        return self.NombreCurso 
    
class Comentario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    curso = models.ForeignKey(Cursos,
    on_delete=models.CASCADE,verbose_name="Curso Elegido")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario") 

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]
    def __str__(self):
        return self.coment 

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]
    def __str__(self):
        return self.mensaje



class Archivos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="Descripcion")
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    update  = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]
        
        def __str__(self):
            return self.archivo