from django.db import models

class Videojuego(models.Model):
    titulo = models.CharField(max_length=10)
    desarrollador = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    plataforma = models.CharField(max_length=50)
    fecha_lanzamiento = models.CharField(max_length=50)

    def __str__(self):
        return f'Videojuego: {self.titulo} {self.desarrollador} {self.genero} {self.plataforma} {self.fecha_lanzamiento}'
