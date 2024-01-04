from django import forms
from .models import Pojeto,Tarefa,RegistroHora

class RegistrodeHoras(forms.ModelForm):
    model = RegistroHora
    fields = ['tarefa','horas_trabalhadas','data_registro']
