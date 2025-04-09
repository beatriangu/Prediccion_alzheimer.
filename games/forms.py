from django import forms
from .models import GameResult

class GameResultForm(forms.ModelForm):
    class Meta:
        model = GameResult
        fields = ['patient', 'score', 'time_spent', 'errors']
        