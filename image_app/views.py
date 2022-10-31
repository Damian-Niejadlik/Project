from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.db import IntegrityError


from image_app.forms import ImageForm
from image_app.models import Image


class ImageView(TemplateView):
    form = ImageForm
    template_name = 'image_app/upload.html'

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('display', kwargs={"fk": request.user}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DisplayView(ListView):
    model = Image
    template_name = 'image_app/display.html'
    context_object_name = 'img'




