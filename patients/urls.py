from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('nuevo/', views.create_patient, name='create_patient'),
    path('lista/', views.list_patients, name='list_patients'),
    path('<str:patient_id>/predicciones/', views.patient_predictions, name='patient_predictions'),
    path('<str:patient_id>/juegos/', views.patient_game_results, name='patient_game_results'),
]


