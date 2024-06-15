from django.urls import path
from . import views

urlpatterns = [
    path('', views.prescription_list, name='prescription_list'),
    path('add_prescription/', views.add_prescription, name='add_prescription'),
    path('add_medication/', views.add_medication, name='add_medication'),
]
