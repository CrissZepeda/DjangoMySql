from django.db import models


# Create your models here.
class Medicos(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Pacientes(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Citas(models.Model):
    Asunto = models.CharField(max_length=100)
    Paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    Medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
