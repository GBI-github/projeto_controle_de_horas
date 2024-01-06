from django.urls import path
from .views import vizu_projeto,vizu_tarefa,viazualizar,registrar_horas


urlpatterns = [
    path('projetos/', vizu_projeto, name='vizu_projeto'),
    path('projetos/<int:id_project>/tarefas/', vizu_tarefa, name='vizu_tarefa'),
    path('registros/', viazualizar, name='viazualizar'),
    path('registrar/', registrar_horas, name='registrar_horas'),
]
