from django.db import models
from agenda.models import Atendimento


class Evolucao(models.Model):
    atendimento = models.OneToOneField(Atendimento, on_delete=models.CASCADE, related_name='evolucao')
    texto = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criada_em']

    def __str__(self):
        return f'Evolução - {self.atendimento.paciente} - {self.atendimento.data}'
