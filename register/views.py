from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.contrib import messages


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
    client = Users

    def get(self, request):

        if self.request.user.is_authenticated:
            return redirect(f"{self.client.user_id}")
        form = self.form_class()
        message = ""
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("dashboard")
        message = "Login failed!"
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )


class ResetPasswordView(View):
    template_name = ""
    client = Users
    success_url = reverse_lazy(f"{client.user_id}")
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
            return redirect(f"{self.client.user_id}")
        else:
            messages.error(request, "Please correct the error below.")
        form = PasswordChangeForm(request.user)
        return render(request, "", {"form": form})
