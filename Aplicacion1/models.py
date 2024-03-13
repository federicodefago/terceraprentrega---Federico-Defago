from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    class Meta:
        ordering = ["nombre", "apellido"]
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

class Personaje(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.nombre}"
    class Meta:
        ordering = ["nombre"]

class Talento(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.nombre}"
    class Meta:
        ordering = ["nombre"]