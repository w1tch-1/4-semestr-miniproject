from django import forms
from .models import User


class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['seller_fullname', 'seller_company_name', 'seller_email', 'is_seller', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(SellerRegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control w-100'})
