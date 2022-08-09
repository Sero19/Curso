
from typing import Optional, Sequence
from django.contrib import admin
from .models import ComentarioContacto, Cursos
from .models import Comentario

class AdministarModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created')
    search_fields: Sequence[str] = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')
    list_per_page = 2
    list_display_links = ('matricula', 'nombre')
    list_editable = ('turno',)
    
    list_per_page=2
    list_display_links=('matricula','nombre')
    list_editable=('turno',)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

class AdministartModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('NombreCurso', 'Descripcion')

    
    
admin.site.register(Cursos, AdministartModelo)




