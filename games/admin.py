from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Game, GameResult

# Acción para exportar a CSV
def export_game_results_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta.model_name}_export.csv'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_game_results_as_csv.short_description = "📤 Exportar seleccionados a CSV"

# Inline para resultados de este juego
class GameResultInline(admin.TabularInline):
    model = GameResult
    extra = 0
    readonly_fields = ('patient', 'score', 'time_spent', 'errors', 'date_played')
    can_delete = False

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'cognitive_area', 'difficulty_level')
    list_filter = ('cognitive_area', 'difficulty_level')
    search_fields = ('name', 'description', 'instructions')
    ordering = ('name',)
    inlines = [GameResultInline]

@admin.register(GameResult)
class GameResultAdmin(admin.ModelAdmin):
    list_display = ('patient', 'game', 'score', 'time_spent', 'errors', 'date_played')
    list_filter = ('game', 'date_played')
    search_fields = ('patient__name', 'game__name')
    ordering = ('-date_played',)
    actions = [export_game_results_as_csv]  # 👈 aquí activas el botón



