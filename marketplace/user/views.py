from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from .forms import UserRegisterForm, UserLoginForm, SellerRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Listing
from .models import User


class RegisterUser(CreateView):
    template_name = 'sign-up.html'
    form_class = UserRegisterForm
    success_url = '/'


class LoginUser(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True


class ProfileView(LoginRequiredMixin, LogoutView,  TemplateView):
    http_method_names = ['post', 'get']
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_listings'] = Listing.objects.filter(user=self.request.user)
        return context


class SellerRegistrationView(UpdateView):
    model = User
    template_name = 'seller_registration.html'
    success_url = '/'
    form_class = SellerRegistrationForm
