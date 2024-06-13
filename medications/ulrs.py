from django.urls import path
from . import views


urlpatterns = [
    path('prescription', views.user_meds, name='medications'),
]