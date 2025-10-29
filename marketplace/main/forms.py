from django import forms
from .models import Listing, Response, Order


from django import forms
from .models import Listing, SubCategory, Types


class ListingCreationForm(forms.ModelForm):
    class Meta:
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

    def __init__(self, *args, **kwargs):
        super(ListingCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['sub_category'].queryset = SubCategory.objects.none()
        self.fields['types'].queryset = Types.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['sub_category'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass

        if 'sub_category' in self.data:
            try:
                sub_category_id = int(self.data.get('sub_category'))
                self.fields['types'].queryset = Types.objects.filter(sub_category_id=sub_category_id)
            except (ValueError, TypeError):
                pass



class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        listing = kwargs.pop('listing')
        super().__init__(*args, **kwargs)
        self.instance.user = user
        self.instance.listing = listing


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.listing = kwargs.pop('listing')
        super().__init__(*args, **kwargs)
        self.instance.user = self.user
        self.instance.title = self.listing.title
        self.instance.price = self.listing.price

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            instance.listing.add(self.listing)
        return instance
