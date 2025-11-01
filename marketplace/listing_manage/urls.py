from django.urls import path
from . import views


urlpatterns = [
    path('profile/listing-manage-overview/', views.ListingsManageOverview.as_view(), name='listing-manage-overview'),
    path('profile/listing-manage/<int:pk>/', views.ListingManage.as_view(), name='listing-manage')
]
