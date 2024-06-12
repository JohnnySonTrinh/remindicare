from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_profile, name='profiles'),
    path('caretaker/', views.caregiver_user, name='caretaker_user'),
]