from django.db import models

# Create your models here.
class Marca(models.Model):
    id_marca    = models.AutoField(db_column='idMarca', primary_key=True)
    marca       = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return str(self.marca)


class Producto(models.Model):
    codprod     = models.AutoField(db_column='idProducto', primary_key=True)
    nombre      = models.CharField(max_length=60)
    titulo      = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=700)
    foto        = models.ImageField()
    marca       = models.ForeignKey('Marca', on_delete=models.CASCADE,db_column='idMarca')
    stock       = models.IntegerField()
    precio      = models.IntegerField()
    fec_salida  = models.DateField(blank=False,null=False)

    def __str__(self):
        return str(self.titulo)