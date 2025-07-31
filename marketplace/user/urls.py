from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'user'

urlpatterns = [
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
