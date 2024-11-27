from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    sexo = models.CharField(max_length=50)
    localidad = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    prepa_procedencia = models.CharField(max_length=250, null=True, blank= True)
    institucion_educativa = models.CharField(max_length=255)
    programa_educativo = models.CharField(max_length=255)
    semestre = models.CharField(max_length=50)
    liderazgo_kurt_lewin = models.CharField(max_length=50)
    liderazgo_daniel_goleman = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre