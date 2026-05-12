from django.conf import settings
from django.db import models

ESPECIALIDADES_CHOICES = [
    ('', 'Selecione uma especialidade'),
    ('Fonoaudiologia', 'Fonoaudiologia'),
    ('Terapia Ocupacional', 'Terapia Ocupacional'),
    ('Fisioterapia', 'Fisioterapia'),
    ('Psicologia', 'Psicologia'),
    ('Psicopedagogia', 'Psicopedagogia'),
    ('Neuropsicologia', 'Neuropsicologia'),
    ('Musicoterapia', 'Musicoterapia'),
    ('Hidroterapia', 'Hidroterapia'),
    ('ABA (Análise do Comportamento Aplicada)', 'ABA (Análise do Comportamento Aplicada)'),
    ('Educação Especial', 'Educação Especial'),
    ('Neuropediatria', 'Neuropediatria'),
    ('Nutrição', 'Nutrição'),
]


class Terapeuta(models.Model):
    nome = models.CharField(max_length=150)
    especialidades = models.CharField(
        max_length=255, blank=True, null=True,
        choices=ESPECIALIDADES_CHOICES,
    )
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
