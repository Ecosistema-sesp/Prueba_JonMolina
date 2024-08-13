from django.db import models

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return self.nombreUsuario

class Beneficiario(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    poblacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Chaleco(models.Model):
    serial = models.IntegerField(primary_key=True)
    beneficiario_cedula = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.serial)
