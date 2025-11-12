from django.views.generic.edit import UpdateView
from django.contrib.auth.views import TemplateView
from django.views.generic.detail import DetailView
from .forms import SellerRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Listing
from cart.models import CartItem
from .models import User


class ProfileView(LoginRequiredMixin,  TemplateView):
    http_method_names = ['post', 'get']
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_listings'] = Listing.objects.filter(user=self.request.user)
        context['cart_items'] = CartItem.objects.filter(user=self.request.user)
        return context


class SellerRegistrationView(UpdateView):
    model = User
    template_name = 'seller_registration.html'
    success_url = '/profile'
    form_class = SellerRegistrationForm


class UserProfileView(DetailView):
    model = User
    template_name = 'profile-view.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_listings'] = Listing.objects.filter(user=self.kwargs['pk'])
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = [
        'seller_fullname',
        'seller_company_name',
        'seller_email',
        'profile_picture',
    ]
    success_url = '/profile'
    template_name = 'profile-edit.html'

    def get_object(self):
        return self.request.user
