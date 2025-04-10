from django.urls import path
from . import views

app_name = 'predictions'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ajax/filtered/', views.filtered_predictions_ajax, name='filtered_predictions_ajax'),  # AJAX para filtros
    path('exportar/', views.export_predictions_csv, name='export_predictions_csv'),
    path('resultado/<int:pk>/', views.prediction_result, name='prediction_result'),  # Detalle de predicción
]




