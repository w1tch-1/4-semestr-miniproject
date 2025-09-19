from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Listing, Response, Category
from main.forms import ListingCreationForm, ResponseForm, OrderCreateForm
from django.urls import reverse_lazy
from .filters import ShopFilter

from render_block import render_block

from django.http import JsonResponse
from .models import SubCategory, Types


class Index(FilterView):
    model = Listing
    template_name = 'index.html'
    context_object_name = 'listing'
    filterset_class = ShopFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_filterset(self, filterset_class):
        self.filterset_class.base_filters['category'].queryset = Category.objects.all()
        return super().get_filterset(filterset_class)

    def get(self, request, *args, **kwargs):
        self.filterset = self.get_filterset(self.get_filterset_class())
        if not self.filterset.is_bound or self.filterset.is_valid() or not self.get_strict():
            self.object_list = self.filterset.qs
        else:
            self.object_list = self.filterset.queryset.none()

        context = self.get_context_data(
            filter=self.filterset,
            object_list=self.object_list
        )

        if self.request.GET.get('is_filter'):
            return render_block(request, self.template_name, 'listing', context)

        return self.render_to_response(context)


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


def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)


def load_types(request):
    sub_category_id = request.GET.get('sub_category')
    types = Types.objects.filter(sub_category_id=sub_category_id).values('id', 'name')
    return JsonResponse(list(types), safe=False)


class ResponseCreateView(CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'partials/response.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        self.listing = Listing.objects.get(id=self.kwargs['listing_id'])
        kwargs.update(
            {
                'user': self.request.user,
                'listing': Listing.objects.get(id=self.kwargs['listing_id'])
            }
        )
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responses'] = self.listing.responses.all()
        return context

    def form_valid(self, form):
        form.save()
        context = {'responses': self.listing.responses.all()}
        return render_block(self.request, 'partials/response.html', 'responses_list', context)


class OrderCreateView(CreateView):
    form_class = OrderCreateForm
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        self.listing = Listing.objects.get(id=self.kwargs['listing_id'])
        kwargs.update(
            {
                'listing': self.listing,
            }
        )
        kwargs['user'] = self.request.user
        return kwargs
