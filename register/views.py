from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, CreateView
from django.contrib import messages

import register.models
from register.forms import UserRegisterForm, LoginForm, PasswordChangingForm
from register.models import Users


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'register/register.html'
    success_url = reverse_lazy("login")
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


class LoginView(View):
    template_name = 'register/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            client = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if client is not None:
                login(request, client)
                return HttpResponseRedirect(reverse("display", kwargs={'fk': request.user}))
                # return HttpResponseRedirect(reverse("display", kwargs={"fk": self.request.user.user_id}))
        message = "Login failed!"
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )


class ResetPasswordView(View):
    template_name = ""
    client = Users
    success_url = reverse_lazy("login")
    form_class = PasswordChangingForm

    def get(self, request):
        form = self.form_class(User)
        message = ""
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return HttpResponseRedirect(reverse("display"))
        else:
            messages.error(request, "Please correct the error below.")
        form = PasswordChangeForm(request.user)
        return render(request, "", {"form": form})


class BaseView(View):
    template_name = "register/home.html"

    def get(self, request):
        return render(request, self.template_name)
