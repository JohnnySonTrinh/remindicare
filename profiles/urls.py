from django.urls import path
from . import views


urlpatterns = [
    path('', views.Profiles.as_view(), name='profiles'),   
    path('caretaker/', views.caregiver_user, name='caretaker_user'),
]