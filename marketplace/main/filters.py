import django_filters
from .models import Listing, Category


class ShopFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search', label='Search')
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        field_name='category',
        label='Category',
        empty_label='All'
    )
    price_range = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')

    class Meta:
        model = Listing
        fields = ['search', 'category', 'price_range']

    def filter_search(self, queryset, name, value):
        if value:
            return queryset.filter(title__icontains=value)
        return queryset
