from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('nuevo/', views.create_patient, name='create_patient'),
    path('lista/', views.list_patients, name='list_patients'),  # ← nuevo
]

