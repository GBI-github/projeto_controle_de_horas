from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projeto(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    nome = models.CharField(max_length=50)
    projeto = models.ForeignKey(Projeto,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class RegistroHora(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tarefa = models.ForeignKey(Tarefa,on_delete=models.CASCADE)
    horas_trabalhadas = models.DecimalField(max_digits= 5, decimal_places= 2 )
    data_registrada = models.DateField()

    def __str__(self):
        return(f"{self.usuario.username}- {self.tarefa.nome}- {self.data_registrada}")


    
    