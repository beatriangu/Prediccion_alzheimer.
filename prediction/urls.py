from django.urls import path
from . import views

app_name = 'predictions'

urlpatterns = [
    path('<int:prediction_id>/', views.show_result, name='show_result'),
    path('dashboard/', views.dashboard, name='dashboard'),
]


