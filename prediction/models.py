from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from patients.models import Patient

class Prediction(models.Model):
    RISK_LEVEL_CHOICES = [
        ('bajo', 'Riesgo Bajo'),
        ('medio', 'Riesgo Medio'),
        ('alto', 'Riesgo Alto'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='predictions')
    risk_level = models.CharField(max_length=10, choices=RISK_LEVEL_CHOICES, verbose_name="Nivel de riesgo")
    confidence_score = models.FloatField(
        verbose_name="Puntuación de confianza",
        validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
    date_predicted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.risk_level} - {self.date_predicted.strftime('%Y-%m-%d')}"

class Recommendation(models.Model):
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE, related_name='recommendations')
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)],
        verbose_name="Prioridad"
    )

    def __str__(self):
        return f"{self.prediction.patient.name} - {self.title}"
