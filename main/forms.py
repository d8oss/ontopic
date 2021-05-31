from django import forms
from django.forms import Textarea, TextInput


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
