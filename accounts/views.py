from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from . import forms


class TopView(TemplateView):
  template_name = "accounts/top.html"


class HomeView(TemplateView):
  template_name = "accounts/home.html"


class LoginView(LoginView):
  form_class = forms.LoginForm
  template_name = "accounts/login.html"


class LogoutView(LogoutView):
  template_name = "accounts/login.html"
