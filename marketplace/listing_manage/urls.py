from django.urls import path
from . import views


urlpatterns = [
    path('profile/listing-manage-overview/', views.ListingsManageOverview.as_view(), name='listing-manage-overview'),
    path('profile/listing-manage/<int:pk>/', views.ListingManageView.as_view(), name='listing-manage'),
    path('profile/listing-manage/<int:pk>/update/', views.ListingUpdateView.as_view(), name='listing-update'),
    path('profile/listing-manage/<int:pk>/delete/', views.ListingDeleteView.as_view(), name='listing-delte')
]
