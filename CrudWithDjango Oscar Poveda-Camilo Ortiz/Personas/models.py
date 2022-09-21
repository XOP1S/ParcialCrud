from importlib.util import module_for_loader
from django.db import models

# Create your models here.


class Paciente(models.Model):
    codigo=models.CharField(primary_key=True, max_length=20)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.PositiveBigIntegerField()
    peso=models.PositiveBigIntegerField()
    bpm=models.PositiveBigIntegerField()
    stress=models.PositiveBigIntegerField()
    oxigeno=models.PositiveBigIntegerField()

    
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre, self.codigo)