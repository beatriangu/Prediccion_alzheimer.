from django.contrib import admin
from .models import Patient, ClinicalData
from prediction.models import Prediction
from games.models import GameResult

# Inline para predicciones
class PredictionInline(admin.TabularInline):
    model = Prediction
    extra = 0
    readonly_fields = ('risk_level', 'confidence_score', 'date_predicted')
    can_delete = False

# Inline para resultados de juegos
class GameResultInline(admin.TabularInline):
    model = GameResult
    extra = 0
    readonly_fields = ('game', 'score', 'errors', 'time_spent', 'date_played')
    can_delete = False

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id_patient', 'name', 'age', 'gender', 'education_level', 'occupation', 'created_at')
    list_filter = ('gender', 'education_level', 'created_at')
    search_fields = ('name', 'id_patient', 'occupation')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [PredictionInline, GameResultInline]  # 👈 Aquí los añadimos

@admin.register(ClinicalData)
class ClinicalDataAdmin(admin.ModelAdmin):
    list_display = ('patient', 'data_type', 'value', 'date_recorded')
    list_filter = ('data_type', 'date_recorded')
    search_fields = ('patient__name', 'data_type', 'value')
    ordering = ('-date_recorded',)
