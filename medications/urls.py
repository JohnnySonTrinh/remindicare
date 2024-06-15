from django.urls import path
from . import views

urlpatterns = [
    path('', views.prescription_list, name='prescription_list'),
    path('add_prescription/', views.add_prescription, name='add_prescription'),
    path('add_medication/', views.add_medication, name='add_medication'),
    path('add_intake_schedule/<int:prescription_id>/<int:medication_id>/', views.add_intake_schedule, name='add_intake_schedule'),
    path('schedule_list/', views.schedule_list, name='schedule_list'),
]
