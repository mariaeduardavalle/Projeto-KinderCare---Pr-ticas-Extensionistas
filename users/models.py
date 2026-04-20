from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    RECEPCAO = 'recepcao'
    TERAPEUTA = 'terapeuta'
    COORDENACAO = 'coordenacao'

    ROLE_CHOICES = [
        (RECEPCAO, 'Recepção'),
        (TERAPEUTA, 'Terapeuta'),
        (COORDENACAO, 'Coordenação'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=RECEPCAO)

    def __str__(self):
        return f'{self.get_full_name() or self.username} ({self.get_role_display()})'
