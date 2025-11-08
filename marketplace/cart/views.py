from .models import CartItem
from main.models import Listing
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView
from django.shortcuts import redirect, get_object_or_404


class CartAddView(CreateView):
    model = CartItem
    template_name = 'listing-details.html'
    fields = []

    def post(self, request, *args, **kwargs):
        listing_id = kwargs.get('listing_id')
        listing = get_object_or_404(Listing, id=listing_id)

        cart_item, created = CartItem.objects.get_or_create(
            listing=listing,
            user=request.user,
        )
        cart_item.quantity += 1
        cart_item.save()
        return redirect('user:profile')
    

class CartRemoveView(DeleteView):
    model = CartItem
    success_url = '/'
    template_name = 'profile.html'
