from django.contrib import admin
from .models import Game, GameResult

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
    inlines = [GameResultInline]  # 👈 añadimos la vista de resultados

@admin.register(GameResult)
class GameResultAdmin(admin.ModelAdmin):
    list_display = ('patient', 'game', 'score', 'time_spent', 'errors', 'date_played')
    list_filter = ('game', 'date_played')
    search_fields = ('patient__name', 'game__name')
    ordering = ('-date_played',)

