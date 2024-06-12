from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_profile, name='profiles'),
    path('caregiver/', views.caregiver_user, name='caregiver_user'),
]