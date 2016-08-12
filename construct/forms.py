from django.forms import ModelForm
from django import forms
from .models import Application

class ApplicationForm(ModelForm):
    author_name = forms.CharField(label='name ', widget=forms.TextInput(attrs={"class":"full", "name":"name", "id":"name ", "type":"text"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':"full", "name":"email", "id":"email"}))
    service = forms.CharField(widget=forms.TextInput(attrs={"class":"  full ", "name":"person_num", "id":"person_num"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"cols":"10", "rows":"10", "name":"message", "id":"message", "class":" full "}))
    datetime = forms.CharField(widget=forms.TextInput(attrs={"class":" full ", "name":"datepicker", "id":"datepicker " }))
    class Meta:
        model = Application
        fields = ['author_name', 'email',	'service', 'message', 'datetime']