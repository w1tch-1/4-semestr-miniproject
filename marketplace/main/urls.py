from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('listing-details/<int:pk>/', views.ListingDetailView.as_view(), name='listing-detail'),
    path('listing-create/', views.ListingCreateView.as_view(), name='listing-create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
