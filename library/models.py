from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=30)
	genre = models.ForeignKey(Genre)

class Book(models.Model):
	title = models.CharField(max_length=30)
	genre = models.ManyToManyField(Genre)
	author = models.ForeignKey(Author)

	def __unicode__(self):
		return self.title

class ReadBook(models.Model):
	genre = models.ForeignKey(Genre)
	books = models.ManyToManyField(Book)
