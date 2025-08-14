from django.contrib import admin
from .models import Post, Categoria, Autor

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_creacion')
    search_fields = ('nombre',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'activo', 'fecha_creacion')
    list_filter = ('categoria', 'activo', 'fecha_creacion')
    search_fields = ('titulo', 'contenido')