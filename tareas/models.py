from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    creada_en = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')
    
    def __str__(self):
        return f'{self.titulo} ({self.usuario.username})'
