from django import forms


class UrlForm(forms.Form):   # http://pythoncentral.io/how-to-use-python-django-forms/
    orig = forms.CharField(max_length=256)
    created_at = forms.DateTimeField()
