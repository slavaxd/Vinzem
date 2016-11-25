# coding: utf-8
from datetime import datetime


from django.db import models

from autoslug import AutoSlugField

from ckeditor.fields import RichTextField

#from taggit.managers import TaggableManager

class News(models.Model):
	image = models.ImageField(upload_to='static/img')
	title = models.CharField(max_length=100)
	text = RichTextField(max_length=5000)#models.CharField(max_length=5000)
	
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
	event_date = models.DateTimeField(default=datetime.now, blank=True,  verbose_name = u"Дата події")
	created_at = models.DateTimeField(auto_now_add=True)
	is_published = models.BooleanField()
	description = models.TextField(max_length=100, default="")
	

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
		return u"{0} від {1} ({2})".format(self.message, self.author_name, self.email)

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
	text = RichTextField(max_length=5000)#models.CharField(max_length=5000)
	created_at = models.DateTimeField(auto_now_add=True)
	price = models.IntegerField()


	CATEGORY_CHOICES = (
		('0', 'Землевпорядні роботи'),
		('1', 'Землеоціночні роботи'),
		('2', 'Геодезичні роботи'),
		('3', 'Інші послуги')
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
	description = RichTextField(max_length=5000)#models.TextField(max_length=5000)

	def __unicode__(self):
		return self.name

	class Meta():
		verbose_name = u"Людина"
		verbose_name_plural = u"Люди"


class IndexBehindLink(models.Model):
        description = RichTextField(max_length=100000)#models.TextField(max_length=5000)

        def __unicode__(self):
                return u"Поле внизу з HTML"

        class Meta():
                verbose_name = u"Поле внизу з HTML"
		verbose_name_plural = u"Поле внизу з HTML"


class WorkHours(models.Model):
        description = RichTextField(max_length=100000)#models.TextField(max_length=5000)

        def __unicode__(self):
                return u"(Контакти) Поле для годин роботи та місцезнаходження"

        class Meta():
                verbose_name = u"(Контакти) Поле для годин роботи та місцезнаходження"
                verbose_name_plural = u"(Контакти) Поле для годин роботи та місцезнаходження"

