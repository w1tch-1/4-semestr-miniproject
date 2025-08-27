from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Listing
from main.forms import ListingCreationForm
from django.urls import reverse_lazy


class Index(ListView, FilterView):
    model = Listing
    template_name = 'index.html'
    context_object_name = 'listing'


class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing-details.html'
    context_object_name = 'listing'


class ListingCreateView(CreateView):
    template_name = 'create-listing.html'
    form_class = ListingCreationForm
    success_url = reverse_lazy('user:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

