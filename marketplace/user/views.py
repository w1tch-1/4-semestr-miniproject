from django.views.generic.edit import UpdateView
from django.contrib.auth.views import TemplateView
from .forms import SellerRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Listing
from .models import User


class ProfileView(LoginRequiredMixin,  TemplateView):
    http_method_names = ['post', 'get']
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_listings'] = Listing.objects.filter(user=self.request.user)
        return context


class SellerRegistrationView(UpdateView):
    model = User
    template_name = 'seller_registration.html'
    success_url = '/profile'
    form_class = SellerRegistrationForm
