from django.core.management.base import BaseCommand
from faker import Faker
import random
from games.models import Game, GameResult
from patients.models import Patient
from prediction.models import Prediction, Recommendation

class Command(BaseCommand):
    help = 'Puebla la base de datos con datos ficticios (pacientes, juegos, resultados, predicciones)'

    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')

        def create_fake_patients(n=20):
            self.stdout.write("🧍‍♂️ Creando pacientes...")
            for _ in range(n):
                Patient.objects.create(
                    id_patient=fake.unique.bothify(text='???-#####'),
                    name=fake.name(),
                    age=random.randint(60, 90),
                    gender=random.choice(['M', 'F', 'O']),
                    education_level=random.choice(['primaria', 'secundaria', 'universidad', 'postgrado']),
                    occupation=fake.job()
                )

        def create_fake_games():
            self.stdout.write("🎮 Creando juegos...")
            areas = ['memoria', 'atencion', 'lenguaje', 'funcion_ejecutiva', 'razonamiento']
            for i in range(5):
                Game.objects.create(
                    name=f"Juego {i+1}",
                    description=fake.paragraph(),
                    cognitive_area=random.choice(areas),
                    instructions=fake.sentence(),
                    difficulty_level=random.randint(1, 5)
                )

        def create_fake_game_results():
            self.stdout.write("📊 Creando resultados de juegos...")
            patients = Patient.objects.all()
            games = Game.objects.all()
            for patient in patients:
                for game in random.sample(list(games), k=random.randint(2, len(games))):
                    GameResult.objects.create(
                        patient=patient,
                        game=game,
                        score=round(random.uniform(0, 100), 2),
                        time_spent=random.randint(30, 300),
                        errors=random.randint(0, 10)
                    )

        def create_fake_predictions():
            self.stdout.write("🧠 Creando predicciones y recomendaciones...")
            levels = ['bajo', 'medio', 'alto']
            for patient in Patient.objects.all():
                pred = Prediction.objects.create(
                    patient=patient,
                    risk_level=random.choice(levels),
                    confidence_score=round(random.uniform(0.6, 0.99), 2)
                )
                for _ in range(random.randint(1, 3)):
                    Recommendation.objects.create(
                        prediction=pred,
                        title=fake.sentence(nb_words=3),
                        description=fake.paragraph(),
                        priority=random.randint(1, 3)
                    )

        # Ejecutar funciones
        create_fake_patients()
        create_fake_games()
        create_fake_game_results()
        create_fake_predictions()
        self.stdout.write(self.style.SUCCESS("✅ ¡Datos ficticios creados con éxito!"))

