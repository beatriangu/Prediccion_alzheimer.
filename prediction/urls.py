from django.urls import path
from . import views

app_name = 'predictions'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('exportar/', views.export_predictions_csv, name='export_predictions_csv'),
    path('<int:prediction_id>/', views.show_result, name='show_result'),
]




