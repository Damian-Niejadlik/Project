from django.shortcuts import render
from django.views import View
from django.forms import ImageField


class ImageView(View):
    template_name = ''
    form_class = ImageField

    def get(self, request):
        pass


