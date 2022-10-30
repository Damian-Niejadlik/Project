from django import forms

from aplikacja.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_name', 'image', 'comment']
