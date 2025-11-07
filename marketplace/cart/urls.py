from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('listing/<int:listing_id>/add-cart/', views.CartAddView.as_view(), name='add_to_cart'),
    path('profile/', views.CartView.as_view(), name='cart-view'),
]