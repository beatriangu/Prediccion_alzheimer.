from django.contrib import admin
from .models import Prediction, Recommendation

class RecommendationInline(admin.TabularInline):
    model = Recommendation
    extra = 0
    readonly_fields = ('title', 'description', 'priority')
    can_delete = False

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'risk_level', 'confidence_score', 'date_predicted')
    list_filter = ('risk_level', 'date_predicted')
    search_fields = ('patient__name',)
    ordering = ('-date_predicted',)
    readonly_fields = ('date_predicted',)
    inlines = [RecommendationInline]

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('prediction', 'title', 'priority')
    list_filter = ('priority',)
    search_fields = ('title', 'description', 'prediction__patient__name')
