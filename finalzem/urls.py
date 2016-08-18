"""finalzem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('construct.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


<<<<<<< HEAD
#urlpatterns += staticfiles_urlpatterns()
=======
urlpatterns += staticfiles_urlpatterns()
>>>>>>> 5dcff49c0da17337ae91b49022c05e6163db5954
