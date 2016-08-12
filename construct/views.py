# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .models import News, GalleryImage, StaticPage, Application, Slider

from .forms import ApplicationForm

def index(request):
	sliders = Slider.objects.order_by('-id')[:3]
	template = loader.get_template("index.html")
	return HttpResponse(template.render(locals(), request))

def services(request):
	pass

def single_service(request, service_id):
	pass

def application(request):
	pass	

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
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplicationForm()

    return render(request, 'contact.html', {'form': form})

def static_page(request, page_slug):
	page = StaticPage(slug=page_slug)
	template = loader.get_template("static_page.html")
	return HttpResponse(template.render(locals(), request))
