from django.db import models
from django.utils import timezone

# Create your models here.

class Pregunta(models.Model):
	"""docstring for Pregunta"models.Modelf __init__(self, arg):"""

	asunto = models.CharField(max_length=200)
	descripcion = models.TextField()
	fecha_publicacion= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.asunto

	def publicado_hoy(self):
		return self.fecha_publicacion.date() == timezone.now().date()


	publicado_hoy.boolean=True
	publicado_hoy.descripcion_corta ='¿Preguntado hoy?'



class Respuesta(models.Model):
	"""docstring for Respuesta"""
	Pregunta = models.TextField()
	contenido = models.TextField()
	mejor_respuesra = models.BooleanField("Respuesta preferida",default=False)

	def __str__(self):
		return self.contenido
		