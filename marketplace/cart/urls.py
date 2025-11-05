from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:pk>/', views.CartAddView.as_view(), name='add_to_cart'),
]