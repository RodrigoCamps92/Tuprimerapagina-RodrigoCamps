from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    biografia = models.TextField(blank=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"