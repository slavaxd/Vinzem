# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
import random

from .models import News, GalleryImage, StaticPage, Application, Slider, Service, Person

from .forms import ApplicationForm

def index(request):
	result = {}
	categories = []
	for x in range(4):
		category_size = Service.objects.filter(category=str(x)).count()
		r = random.randint(0, category_size-1)
		categories.append(Service.objects.filter(category=str(x))[r])
	#print categories
	sliders = Slider.objects.order_by('id')[:4]
	result['categories'] = categories
	result['sliders'] = sliders
	template = loader.get_template("index.html")
	print result
	return HttpResponse(template.render(result, request))

def services(request):

	result = {}
	categories = {}
	for x in range(4):
		cat = Service.objects.filter(category=str(x))[0].category
		categories[cat] = Service.objects.filter(category=str(x))
	result["categories"] = categories
	template = loader.get_template("services.html")
	result["names"] = ['Землевиорні роботи', 'Землеоціночні роботи', 'Якісь ще роботи', 'Останні роботи']
	print result
	return HttpResponse(template.render(result, request))

def single_service(request, service_id):
    service = Service.objects.get(id=service_id)
    template = loader.get_template("single_service.html")
    return HttpResponse(template.render(locals(), request))

def application(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApplicationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            appl = form.save(commit=False)
            appl.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplicationForm()

    return render(request, 'application.html', {'form': form})

def news_index(request):
	latest_news_list = News.objects.order_by('-id')[:3]
	template = loader.get_template("news_index.html")
	return HttpResponse(template.render(locals(), request))

def single_news(request, news_id):
	news = News.objects.get(id=news_id)
	template = loader.get_template("single_news.html")
	return HttpResponse(template.render(locals(), request))

def gallery(request):
	images = GalleryImage.objects.order_by('-id')
	template = loader.get_template("gallery.html")
	return HttpResponse(template.render(locals(), request))

def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApplicationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            appl = form.save(commit=False)
            appl.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplicationForm()

    return render(request, 'contact.html', {'form': form})

def static_page(request, page_slug):
	page = StaticPage(slug=page_slug)
	template = loader.get_template("static_page.html")
	return HttpResponse(template.render(locals(), request))

def structure(request):
	people = Person.objects.all()
	template = loader.get_template("structure.html")
	return HttpResponse(template.render(locals(), request))
