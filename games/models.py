from django.db import models
from patients.models import Patient
from django.core.validators import MinValueValidator, MaxValueValidator

class Game(models.Model):
    COGNITIVE_AREA_CHOICES = [
        ('memoria', 'Memoria'),
        ('atencion', 'Atención'),
        ('lenguaje', 'Lenguaje'),
        ('funcion_ejecutiva', 'Función Ejecutiva'),
        ('razonamiento', 'Razonamiento'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nombre del juego")
    description = models.TextField(verbose_name="Descripción")
    cognitive_area = models.CharField(max_length=20, choices=COGNITIVE_AREA_CHOICES, verbose_name="Área cognitiva")
    instructions = models.TextField(verbose_name="Instrucciones")
    difficulty_level = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Nivel de dificultad"
    )
    
    def __str__(self):
        return self.name

class GameResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='game_results')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.FloatField(verbose_name="Puntuación")
    time_spent = models.IntegerField(verbose_name="Tiempo empleado (segundos)")
    errors = models.IntegerField(verbose_name="Número de errores")
    date_played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.game.name} - {self.date_played.strftime('%Y-%m-%d')}"
