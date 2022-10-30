from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView

from aplikacja.forms import ImageForm
from aplikacja.models import Image


class ImageView(TemplateView):
    form = ImageForm
    template_name = 'aplikacja/upload.html'

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DisplayView(DetailView):
    model = Image
    template_name = 'display.html'
    context_object_name = 'img'
