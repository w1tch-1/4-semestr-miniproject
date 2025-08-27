from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('seller-registration/<int:pk>', views.SellerRegistrationView.as_view(), name='seller-registration')
]

