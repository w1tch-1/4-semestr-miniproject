from django.urls import path


from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('listing-details/<int:pk>/', views.ListingDetailView.as_view(), name='listing-detail'),
    path('listing-create/', views.ListingCreateView.as_view(), name='listing-create'),
]
