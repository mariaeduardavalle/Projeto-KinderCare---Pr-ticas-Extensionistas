from django.db import models
from terapeutas.models import Terapeuta


class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, blank=True)
    responsavel = models.CharField(max_length=150)
    contato = models.CharField(max_length=20)
    observacoes = models.TextField(blank=True)
    terapeutas_responsaveis = models.ManyToManyField(Terapeuta, blank=True, related_name='pacientes')

    def __str__(self):
        return self.nome


class TerapiaPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='terapias')
    nome_terapia = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.paciente.nome} - {self.nome_terapia}'
