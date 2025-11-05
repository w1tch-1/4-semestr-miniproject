from django.contrib.auth.views import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from main.models import Listing

class ListingsManageOverview(TemplateView):
    http_method_names = ['post', 'get']
    template_name = 'listings-manage-overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_listings'] = Listing.objects.filter(user=self.request.user)
        return context
    

class ListingManageView(DetailView):
    model = Listing
    template_name = 'listing_manage.html'
    context_object_name = 'listing'


class ListingUpdateView(UpdateView):
    model = Listing
    fields = [
            'category',
            'sub_category',
            'types',
            'title',
            'price',
            'type_of_price',
            'description',
            'pictures',
            'telephone_number'
        ]
    success_url = '/'
    template_name = 'listing_manage.html'


class ListingDeleteView(DeleteView):
    model = Listing
    success_url = '/'
    template_name = 'listing_manage.html'
