from django.db import models
from pacientes.models import Paciente


class PresencaAula(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='presencas_aula')
    data = models.DateField()
    presente = models.BooleanField(default=False)

    class Meta:
        unique_together = ('paciente', 'data')
        ordering = ['data', 'paciente__nome']
        verbose_name = 'Presença em Aula'
        verbose_name_plural = 'Presenças em Aula'

    def __str__(self):
        status = 'Presente' if self.presente else 'Ausente'
        return f'{self.paciente.nome} - {self.data} - {status}'
