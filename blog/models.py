from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biografia = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.titulo


