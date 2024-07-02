from django.db import models

# Create your models here.

class Cliente(models.Model):
    correo      = models.EmailField(primary_key='True', max_length=100, blank=False, null=False)
    nombre      = models.CharField(max_length=20, blank=False, null=False)
    apellido    = models.CharField(max_length=20, blank=False, null=False)
    contraseña  = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)