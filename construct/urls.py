from django.conf.urls import url

from . import views


urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^services$', views.services, name='services'),
    url(r'^services/(?P<service_id>[0-9]+)$', views.single_service, name='service'),
    url(r'^application$', views.application, name='application'),
    url(r'^news$', views.news_index, name='news_index'),
    url(r'^news/(?P<news_id>[0-9]+)$', views.single_news, name='single_news'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^page/(?P<page_slug>[-\w]+)$', views.static_page, name='static_page'),

]