from django import forms

class UrlForm(forms.Form):
    long_url = forms.CharField(max_length=300)