from django.forms import ModelForm
from django import forms

from image_app.models import Image


class ImageForm(ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Image
        fields = ['image']
