from django.urls import path


from . import views

urlpatterns = [
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
