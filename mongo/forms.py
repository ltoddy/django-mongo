from django import forms

from .models import Mongo


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(), max_length=50)
    password = forms.CharField(widget=forms.TextInput(), max_length=50, empty_value='')
    host = forms.CharField(widget=forms.TextInput(), max_length=50, empty_value='localhost')
    port = forms.IntegerField(widget=forms.TextInput(), min_value=0, max_value=65535)

    class Meta:
        model = Mongo
        fields = ['username', 'password', 'host', 'port']
