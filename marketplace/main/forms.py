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
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'sub_category': forms.Select(attrs={'class': 'form-control'}),
            'types': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'type_of_price': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'pictures': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
