from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('listing/<int:listing_id>/add-cart/', views.CartAddView.as_view(), name='add_to_cart'),
    path('profile/<int:pk>/cart-remove/', views.CartRemoveView.as_view(), name='remove-cart')
]