from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator


User = get_user_model()

# Create your models here.


class MovieList(models.Model):
	"""Modelo de Lista de peliculas por ver"""

	name = models.CharField('Nombre de la Lista', max_length=50, unique=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	movies = models.ManyToManyField('movies.Movie')

	def __str__(self):
		return "'{list}' de {owner}".format(
			list=self.name,
			owner=self.owner.get_full_name()
		)


class Movie(models.Model):
	"""Modelo de Peliculas"""

	name=models.CharField('Nombre de la Pelicula', max_length=100)
	release_date = models.DateField('Fecha de Estreno')
	rate_count = models.PositiveIntegerField('Veces que se ha calificado a la Pelicula', blank=True, null=True)
	rate = models.PositiveIntegerField('Total de calificacion d ela pelicula', blank=True, null=True)
	tags=models.ManyToManyField('movies.Tag')
	studio= models.ForeignKey('movies.Studio', on_delete=models.CASCADE)
	director= models.ForeignKey('movies.Director', on_delete=models.CASCADE)

	def average_rate(self):
		"""Devuelve la calificacion promedio d ela pelicula"""
		#Evita division por 0

		if self.rate_count==0:
			return 0

		else:
			return rate/rate_count


	def __str__(self):
		return self.name


class Tag(models.Model):

	"""Modelo para el Tag"""
	name= models.CharField('Nombre del tag', max_length=20, unique=True)
	def __str__(self):
		return sel.name


class Studio(models.Model):
	"""Modelo de estudio de Cine"""
	
	name= models.CharField(max_length=30, unique=True)

	def __str__(self):
		return sel.name

class Director(models.Model):
	"""Modelo de Director de Cine"""
	
	first_name= models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)

	def get_full_name(self):
		return "{first_name} {last_name}".format(
			first_name=self.first_name,
			last_name= self.last_name
			)

	def __str__(self):
		return self.get_full_name()