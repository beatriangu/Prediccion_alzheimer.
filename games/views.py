from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib import messages
import os
import joblib

from .models import Game, GameResult
from .forms import GameResultForm
from prediction.models import Prediction
from prediction.utils import generar_recomendaciones_automaticas


def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})


def game_result_list(request):
    game_results = GameResult.objects.all()
    return render(request, 'games/game_result_list.html', {'game_results': game_results})


def play_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    if request.method == 'POST':
        form = GameResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.game = game
            result.save()

            try:
                # Cargar modelo y codificador
                model_path = os.path.join(settings.BASE_DIR, 'prediction', 'modelos', 'modelo_alzheimer.pkl')
                encoder_path = os.path.join(settings.BASE_DIR, 'prediction', 'modelos', 'label_encoder.pkl')
                model = joblib.load(model_path)
                encoder = joblib.load(encoder_path)

                # Preparar los datos para predecir
                X = [[result.score, result.errors, result.time_spent]]
                y_pred = model.predict(X)
                y_proba = model.predict_proba(X)

                nivel_riesgo = encoder.inverse_transform(y_pred)[0]
                confianza = max(y_proba[0])  # mayor probabilidad

                # Crear predicción en la base de datos
                prediction = Prediction.objects.create(
                    patient=result.patient,
                    risk_level=nivel_riesgo,
                    confidence_score=round(confianza, 2)
                )

                # 🧠 Generar recomendaciones automáticamente
                generar_recomendaciones_automaticas(prediction)

                return redirect('predictions:show_result', prediction_id=prediction.id)

            except Exception as e:
                messages.error(request, f"Ocurrió un error al generar la predicción: {e}")
                return redirect('games:game_list')

    else:
        form = GameResultForm()

    return render(request, 'games/play_game.html', {'form': form, 'game': game})
