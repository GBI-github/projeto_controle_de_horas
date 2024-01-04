from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pojeto,Tarefa,RegistroHora
from .forms import RegistrodeHoras

def viazualizar(request):
    registro = RegistroHora.objects.filter(usuario=request.user)
    return render(request, 'controle/vizualizar_registros.html', {'registro': registro})

# 
