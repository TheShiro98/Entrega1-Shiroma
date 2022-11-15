from django.db import models

# Create your models here.
class Ficcion(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    titulo = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    fecha = models.DateField()


class Terror(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    titulo = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    fecha = models.DateField()


class Novela(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    titulo = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    fecha = models.DateField()