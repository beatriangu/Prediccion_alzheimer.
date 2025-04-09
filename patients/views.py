from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PatientForm
from .models import Patient
from prediction.models import Prediction
from games.models import GameResult

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            id_patient = form.cleaned_data.get('id_patient')
            if Patient.objects.filter(id_patient=id_patient).exists():
                messages.error(request, f"Ya existe un paciente registrado con el ID: {id_patient}.")
            else:
                form.save()
                messages.success(request, "✅ Paciente registrado correctamente.")
                return redirect('games:game_list')
        else:
            messages.warning(request, "Por favor, revisa los datos del formulario.")
    else:
        form = PatientForm()

    return render(request, 'patients/patient_create.html', {'form': form})

def list_patients(request):
    patients = Patient.objects.all().order_by('-created_at')
    return render(request, 'patients/patient_list.html', {'patients': patients})

def patient_predictions(request, patient_id):
    patient = get_object_or_404(Patient, id_patient=patient_id)
    predictions = patient.predictions.all().order_by('-date_predicted')
    return render(request, 'patients/patient_predictions.html', {
        'patient': patient,
        'predictions': predictions
    })

def patient_game_results(request, patient_id):
    patient = get_object_or_404(Patient, id_patient=patient_id)
    game_results = patient.game_results.all().order_by('-date_played')
    return render(request, 'patients/patient_game_results.html', {
        'patient': patient,
        'game_results': game_results
    })
