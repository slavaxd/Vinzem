# coding: utf-8
from django.db import models

from autoslug import AutoSlugField
#from taggit.managers import TaggableManager

class News(models.Model):
	image = models.ImageField(upload_to='static/img')
	title = models.CharField(max_length=100)
	text = models.CharField(max_length=5000)
	created_at = models.DateTimeField(auto_now_add=True)
	is_published = models.BooleanField()
	slug = AutoSlugField(populate_from='title', unique_with='created_at__month')

	def __unicode__(self):
		return self.title

	class Meta():
		verbose_name = u"Новина"
		verbose_name_plural = u"Новини"

class GalleryImage(models.Model):

	image = models.ImageField(upload_to='static/img')
	text = models.CharField(max_length=40)
	created_at = models.DateTimeField(auto_now_add=True)
	is_published = models.BooleanField()

	def __unicode__(self):
		return self.text

	class Meta():
		verbose_name = u"Фотографія"
		verbose_name_plural = u"Фотографії"

class StaticPage(models.Model):
	slug = models.SlugField()
	title = models.TextField(max_length=300)
	content = models.TextField(max_length=5000)

	def __unicode__(self):
		return self.title

	class Meta():
		verbose_name = u"Статична сторінка"
		verbose_name_plural = u"Статичні сторінки"


class Application(models.Model):
	author_name = models.TextField()
	email = models.EmailField()
	datetime = models.TextField()
	service = models.TextField()
	message = models.TextField()

	def __unicode__(self):
		return u"{0} від {1}".format(self.message, self.author_name)

	class Meta():
		verbose_name = u"Заявка"
		verbose_name_plural = u"Заявки"

class Slider(models.Model):
	image = models.ImageField(upload_to='static/img')
	title = models.TextField(max_length=300)
	content = models.TextField(max_length=5000)

	def __unicode__(self):
		return self.title

	class Meta():
		verbose_name = u"Слайдер"
		verbose_name_plural = u"Слайдери"

class Service(models.Model):
	image = models.ImageField(upload_to='static/img')
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=500)
	text = models.CharField(max_length=5000)
	created_at = models.DateTimeField(auto_now_add=True)
	price = models.IntegerField()


	CATEGORY_CHOICES = (
		('0', 'Землевиорні роботи'),
		('1', 'Землеоціночні роботи'),
		('2', 'Якісь ще роботи'),
		('3', 'Останні роботи')
	)
	category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)

	is_published = models.BooleanField()

	def __unicode__(self):
		return self.title

	class Meta():
		verbose_name = u"Послуга"
		verbose_name_plural = u"Послуги"


class Person(models.Model):
	image = models.ImageField(upload_to='static/img')
	name = models.TextField(max_length=300)
	description = models.TextField(max_length=5000)

	def __unicode__(self):
		return self.name

	class Meta():
		verbose_name = u"Людина"
		verbose_name_plural = u"Люди"
