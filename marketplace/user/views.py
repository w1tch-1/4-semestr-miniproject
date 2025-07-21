from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class RegisterUser(CreateView):
    template_name = 'sign-up.html'
    form_class = UserRegisterForm
    success_url = '/'


class LoginUser(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True


class Logout(LogoutView):
    http_method_names = ['post', 'get']
    template_name = 'logout.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
