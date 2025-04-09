import io
import csv
import base64
import matplotlib.pyplot as plt
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.dateparse import parse_date

from .models import Prediction
from patients.models import Patient

def show_result(request, prediction_id):
    prediction = get_object_or_404(Prediction, id=prediction_id)
    return render(request, 'prediction/prediction_result.html', {'prediction': prediction})


def dashboard(request):
    # Filtro por fechas
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    predictions = Prediction.objects.all()

    if start_date:
        predictions = predictions.filter(date_predicted__date__gte=parse_date(start_date))
    if end_date:
        predictions = predictions.filter(date_predicted__date__lte=parse_date(end_date))

    predictions = predictions.order_by('date_predicted')

    latest_patient = Patient.objects.order_by('-created_at').first()
    latest_prediction = predictions.last()  # Última del conjunto filtrado

    # Gráfico 1: Distribución por nivel de riesgo
    levels = ['bajo', 'medio', 'alto']
    counts = [predictions.filter(risk_level=level).count() for level in levels]

    fig1, ax1 = plt.subplots()
    ax1.bar(levels, counts, color=['green', 'orange', 'red'])
    ax1.set_title('Distribución de niveles de riesgo')
    ax1.set_ylabel('Número de predicciones')
    plt.tight_layout()

    buffer1 = io.BytesIO()
    fig1.savefig(buffer1, format='png')
    buffer1.seek(0)
    graphic1 = base64.b64encode(buffer1.getvalue()).decode('utf-8')
    buffer1.close()
    plt.close(fig1)

    # Gráfico 2: Evolución por fecha
    fechas = predictions.values_list('date_predicted', flat=True)
    fechas_formateadas = [f.date() for f in fechas]
    fechas_unicas = sorted(set(fechas_formateadas))
    frecuencias = [fechas_formateadas.count(f) for f in fechas_unicas]

    fig2, ax2 = plt.subplots()
    ax2.plot(fechas_unicas, frecuencias, marker='o')
    ax2.set_title('Predicciones por fecha')
    ax2.set_xlabel('Fecha')
    ax2.set_ylabel('Cantidad')
    ax2.grid(True)
    plt.tight_layout()

    buffer2 = io.BytesIO()
    fig2.savefig(buffer2, format='png')
    buffer2.seek(0)
    graphic2 = base64.b64encode(buffer2.getvalue()).decode('utf-8')
    buffer2.close()
    plt.close(fig2)

    return render(request, 'dashboard.html', {
        'graphic1': graphic1,
        'graphic2': graphic2,
        'total_predictions': predictions.count(),
        'latest_patient': latest_patient,
        'latest_prediction': latest_prediction,
    })


def export_predictions_csv(request):
    # Crear respuesta con tipo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="predicciones_alzheimer.csv"'

    writer = csv.writer(response)
    writer.writerow(['Paciente', 'Nivel de Riesgo', 'Confianza (%)', 'Fecha'])

    for pred in Prediction.objects.all().order_by('-date_predicted'):
        writer.writerow([
            pred.patient.name,
            pred.get_risk_level_display(),
            f"{pred.confidence_score:.2f}",
            pred.date_predicted.strftime("%d/%m/%Y %H:%M")
        ])

    return response
def show_result(request, prediction_id):
    prediction = get_object_or_404(Prediction, id=prediction_id)
    return render(request, 'prediction/prediction_result.html', {'prediction': prediction})
