from django import forms
from .models import Listing


class ListingCreationForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['category',
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
