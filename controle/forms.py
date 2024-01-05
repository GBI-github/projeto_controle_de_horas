from django import forms
from .models import RegistroHora

class RegistrodeHoras(forms.ModelForm):
    class Meta:
        model = RegistroHora
        fields = ['tarefa','horas_trabalhadas','data_registro']
