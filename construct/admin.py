from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

#from django_summernote.admin import SummernoteModelAdmin

from .models import News, GalleryImage, StaticPage, Application, Slider, Service, Person, IndexBehindLink, WorkHours

#admin.site.register(News)
admin.site.register(GalleryImage)
#admin.site.register(StaticPage)
admin.site.register(Application)
admin.site.register(Slider)
admin.site.register(Person)
admin.site.register(IndexBehindLink)
admin.site.register(WorkHours)

#class PersonForm(SummernotModelAdmin):
#    pass

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    image = forms.ImageField()
    title = forms.CharField()
    is_published = forms.BooleanField()

    class Meta:
        model = News
        fields = "__all__"

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


class StaticPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    title = forms.CharField()
    slug = forms.SlugField()
    class Meta:
        model = StaticPage
        fields = "__all__"

class StaticPageAdmin(admin.ModelAdmin):
    form = StaticPageAdminForm

admin.site.register(News, NewsAdmin)
admin.site.register(StaticPage, StaticPageAdmin)
admin.site.register(Service)
