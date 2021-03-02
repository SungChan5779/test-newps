from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.
class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        print(username)
        print(password)
        user = authenticate(self.request, username=username, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
        else:
            print("login is failed")
        return super().form_valid(form)

def LogoutView(request):
    logout(request)

    return redirect(reverse("core:home"))