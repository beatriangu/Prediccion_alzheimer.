from .models import Recommendation

def generar_recomendaciones_automaticas(prediction):
    nivel = prediction.risk_level

    recomendaciones_por_nivel = {
        'bajo': [
            ("🧠 Mantener actividad", "Sigue realizando actividades cognitivas y físicas diarias.", 3),
            ("🥗 Alimentación saludable", "Prioriza frutas, verduras y grasas saludables.", 3),
        ],
        'medio': [
            ("👩‍⚕️ Consultar con especialista", "Pide una revisión detallada de tus funciones cognitivas.", 2),
            ("🏃‍♀️ Ejercicio regular", "Realiza ejercicios cardiovasculares suaves al menos 3 veces por semana.", 2),
        ],
        'alto': [
            ("🚨 Evaluación médica urgente", "Contacta con un profesional de salud cognitiva cuanto antes.", 1),
            ("👨‍👩‍👧 Acompañamiento familiar", "Informa a tu entorno para recibir apoyo.", 1),
            ("📅 Establecer rutinas", "Organiza rutinas para reducir la desorientación.", 2),
        ]
    }

    recomendaciones = recomendaciones_por_nivel.get(nivel, [])

    if not recomendaciones:
        return  # Nivel no reconocido

    for titulo, descripcion, prioridad in recomendaciones:
        Recommendation.objects.create(
            prediction=prediction,
            title=titulo,
            description=descripcion,
            priority=prioridad
        )
