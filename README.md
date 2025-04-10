# 🧠 Predicción de Alzheimer mediante Juegos Interactivos

Este proyecto es una aplicación web construida con Django que permite predecir el nivel de riesgo de Alzheimer en pacientes, utilizando resultados de juegos cognitivos interactivos. Además, genera recomendaciones automáticas personalizadas basadas en el resultado de cada predicción.

## 🚀 Funcionalidades

- Registro y gestión de pacientes
- Juegos clasificados por áreas cognitivas (memoria, atención, etc.)
- Registro de resultados por juego (puntuación, errores, tiempo)
- Generación de predicciones automáticas con modelo de Machine Learning
- Visualización de gráficas interactivas en el dashboard
- Exportación a CSV de predicciones y resultados
- Sistema AJAX para filtros en tiempo real
- Panel de administración completo y visual

## 📊 Dashboard

El sistema cuenta con un dashboard que incluye:

- Total de predicciones realizadas
- Última predicción y último paciente registrado
- Gráficas de:
  - Distribución de niveles de riesgo
  - Evolución de predicciones por fecha
- Filtros por paciente y fecha
- Tabla dinámica con botón de exportar resultados filtrados

## 🧠 Modelo Predictivo

- Entrenado en `scikit-learn`
- Se guarda como `.pkl` y se carga con `joblib`
- Predice el nivel de riesgo (`bajo`, `medio`, `alto`)
- Devuelve también la probabilidad/confianza

## 💡 Recomendaciones automáticas

Después de cada predicción, el sistema genera automáticamente una serie de recomendaciones adaptadas al nivel de riesgo del paciente (ejercicio cognitivo, alimentación, estilo de vida...).

## 🛠️ Tecnologías utilizadas

- Python 3.13
- Django 4+
- SQLite (puede migrarse a PostgreSQL fácilmente)
- Matplotlib (para gráficos embebidos)
- Bootstrap (para interfaz)
- Faker (para generar datos de prueba)
- AJAX y JavaScript para filtros dinámicos

## 🧪 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/beatrizlamiquiz/prediccion-alzheimer.git
cd prediccion-alzheimer

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Crear la base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar el servidor
python manage.py runserver

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

                # ✅ Redirige correctamente a la vista detallada
                return redirect('predictions:prediction_result', pk=prediction.id)

            except Exception as e:
                messages.error(request, f"Ocurrió un error al generar la predicción: {e}")
                return redirect('games:game_list')

    else:
        form = GameResultForm()

    return render(request, 'games/play_game.html', {'form': form, 'game': game})


---

## 🔒 Aviso legal

Esta aplicación es solo con fines educativos y de investigación. No reemplaza diagnóstico clínico ni asesoramiento médico. Se prohíbe su uso con fines terapéuticos sin validación científica adecuada.
