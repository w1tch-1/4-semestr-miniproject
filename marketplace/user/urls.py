from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('seller-registration/<int:pk>', views.SellerRegistrationView.as_view(), name='seller-registration')
]

