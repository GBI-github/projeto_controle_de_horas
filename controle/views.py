from django.shortcuts import render, redirect
from .models import Projeto,Tarefa,RegistroHora
from .forms import RegistrodeHoras

def vizu_projeto(request):
    projetos = Projeto.objects.all()
    return render(request, 'controle/vizualizar_projeto.html', {'projetos': projetos})

def vizu_tarefa(request, id_project):
    projeto = Projeto.objects.get(pk=id_project)
    tarefa = Tarefa.objects.filter(projeto=projeto)
    return render(request, 'controle/vizualizar_tarefa.html',{'tarefa':tarefa})

def viazualizar(request):
    registro = RegistroHora.objects.filter(usuario=request.user)
    return render(request, 'controle/vizualizar_registros.html', {'registro': registro})

def registar_horas(request):
    if request.method == "POST":
        form = RegistrodeHoras(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('vizualizar_registros')
    else:
        form = RegistrodeHoras()
    
    return render(request, 'controle/registro_de_horas.html',{'form' : form})
