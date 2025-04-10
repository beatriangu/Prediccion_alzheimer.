import io
import csv
import base64
import matplotlib
matplotlib.use('Agg')  # 👈 Evita errores en macOS o entornos sin GUI
import matplotlib.pyplot as plt

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.utils.dateparse import parse_date
from django.template.loader import render_to_string

from .models import Prediction
from patients.models import Patient


def prediction_result(request, pk):
    prediction = get_object_or_404(Prediction, pk=pk)
    return render(request, 'prediction/prediction_result.html', {'prediction': prediction})


def dashboard(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    predictions = Prediction.objects.all()
    if start_date:
        predictions = predictions.filter(date_predicted__date__gte=parse_date(start_date))
    if end_date:
        predictions = predictions.filter(date_predicted__date__lte=parse_date(end_date))

    predictions = predictions.order_by('date_predicted')

    latest_patient = Patient.objects.order_by('-created_at').first()
    latest_prediction = predictions.last()

    # --- Gráfico 1: Distribución de niveles de riesgo ---
    levels = ['bajo', 'medio', 'alto']
    counts = [predictions.filter(risk_level=lvl).count() for lvl in levels]

    fig1, ax1 = plt.subplots(figsize=(5, 3))
    ax1.bar(levels, counts, color=['green', 'orange', 'red'])
    ax1.set_title('Distribución de niveles de riesgo')
    ax1.set_ylabel('Número de predicciones')
    plt.tight_layout()

    buffer1 = io.BytesIO()
    fig1.savefig(buffer1, format='png')
    graphic1 = base64.b64encode(buffer1.getvalue()).decode('utf-8')
    buffer1.close()
    plt.close(fig1)

    # --- Gráfico 2: Evolución de predicciones por fecha ---
    fechas = predictions.values_list('date_predicted', flat=True)
    fechas_formateadas = [f.date() for f in fechas]
    fechas_unicas = sorted(set(fechas_formateadas))
    frecuencias = [fechas_formateadas.count(f) for f in fechas_unicas]

    fig2, ax2 = plt.subplots(figsize=(6, 3))
    ax2.plot(fechas_unicas, frecuencias, marker='o')
    ax2.set_title('Predicciones por fecha')
    ax2.set_xlabel('Fecha')
    ax2.set_ylabel('Cantidad')
    ax2.grid(True)
    plt.tight_layout()

    buffer2 = io.BytesIO()
    fig2.savefig(buffer2, format='png')
    graphic2 = base64.b64encode(buffer2.getvalue()).decode('utf-8')
    buffer2.close()
    plt.close(fig2)

    return render(request, 'prediction/dashboard.html', {
        'graphic1': graphic1,
        'graphic2': graphic2,
        'total_predictions': predictions.count(),
        'latest_patient': latest_patient,
        'latest_prediction': latest_prediction,
        'patients': Patient.objects.all(),
    })


def export_predictions_csv(request):
    patient_id = request.GET.get('patient_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    queryset = Prediction.objects.all()
    if patient_id:
        queryset = queryset.filter(patient__id_patient=patient_id)
    if start_date:
        queryset = queryset.filter(date_predicted__date__gte=parse_date(start_date))
    if end_date:
        queryset = queryset.filter(date_predicted__date__lte=parse_date(end_date))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="predicciones_alzheimer.csv"'

    writer = csv.writer(response)
    writer.writerow(['Paciente', 'Nivel de Riesgo', 'Confianza (%)', 'Fecha'])

    for pred in queryset.order_by('-date_predicted'):
        writer.writerow([
            pred.patient.name,
            pred.get_risk_level_display(),
            f"{pred.confidence_score:.2f}",
            pred.date_predicted.strftime("%d/%m/%Y %H:%M")
        ])

    return response


def filtered_predictions_ajax(request):
    patient_id = request.GET.get('patient_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    queryset = Prediction.objects.all()
    if patient_id:
        queryset = queryset.filter(patient__id_patient=patient_id)
    if start_date:
        queryset = queryset.filter(date_predicted__date__gte=parse_date(start_date))
    if end_date:
        queryset = queryset.filter(date_predicted__date__lte=parse_date(end_date))

    queryset = queryset.order_by('-date_predicted')

    html = render_to_string('prediction/includes/predictions_table.html', {
        'predictions': queryset
    })

    return JsonResponse({'html': html})


