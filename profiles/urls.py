from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileView.as_view(), name='profiles'),
    path('accounts/signup/', views.CustomSignupView.as_view(), name='account_signup'),
]