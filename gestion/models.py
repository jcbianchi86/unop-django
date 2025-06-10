from django.db import models

# Create your models here.
from django.db import models

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
