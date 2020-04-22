from django.db import models

# Create your models here.
class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=300)
    fecha_publicacion = models.DateField('Fecha Publicacion')
    def __str__(self):
        return "Pregunta " + self.texto_pregunta

class Alternativa(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete = models.CASCADE)
    texto_alternativa = models.CharField(max_length=300)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return "Alternativa " + self.texto_alternativa + " Pregunta: " + self.pregunta.texto_pregunta
