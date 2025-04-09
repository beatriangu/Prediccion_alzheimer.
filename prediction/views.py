import io
import base64
import matplotlib.pyplot as plt
from django.shortcuts import render, get_object_or_404
from .models import Prediction

def show_result(request, prediction_id):
    prediction = get_object_or_404(Prediction, id=prediction_id)
    return render(request, 'prediction_result.html', {'prediction': prediction})


def dashboard(request):
    predictions = Prediction.objects.all().order_by('date_predicted')

    # -------------------
    # Gráfico 1: Recuento por nivel de riesgo
    # -------------------
    levels = ['bajo', 'medio', 'alto']
    counts = [predictions.filter(risk_level=level).count() for level in levels]

    fig1, ax1 = plt.subplots()
    ax1.bar(levels, counts, color=['green', 'orange', 'red'])
    ax1.set_title('Distribución de niveles de riesgo')
    ax1.set_ylabel('Número de predicciones')

    buffer1 = io.BytesIO()
    plt.tight_layout()
    fig1.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_png1 = buffer1.getvalue()
    buffer1.close()
    graphic1 = base64.b64encode(image_png1).decode('utf-8')
    plt.close(fig1)

    # -------------------
    # Gráfico 2: Predicciones por fecha
    # -------------------
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

    buffer2 = io.BytesIO()
    plt.tight_layout()
    fig2.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_png2 = buffer2.getvalue()
    buffer2.close()
    graphic2 = base64.b64encode(image_png2).decode('utf-8')
    plt.close(fig2)

    return render(request, 'dashboard.html', {
        'graphic1': graphic1,
        'graphic2': graphic2,
        'total_predictions': predictions.count()
    })
