from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('listing-details/<int:pk>/', views.ListingDetailView.as_view(), name='listing-detail'),

    path('listing-create/', views.ListingCreateView.as_view(), name='listing-create'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    path('ajax/load-types/', views.load_types, name='ajax_load_types'),

    path('listing/<int:listing_id>/response/', views.ResponseCreateView.as_view(), name='product-responses'),

    path('listing/<int:listing_id>/create-order/', views.OrderCreateView.as_view(), name='listing-order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
