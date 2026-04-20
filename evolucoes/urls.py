from django.urls import path
from . import views

urlpatterns = [
    path('atendimento/<int:atendimento_pk>/', views.evolucao_create_or_update, name='evolucao_create_or_update'),
    path('paciente/<int:paciente_pk>/', views.historico_evolucoes_paciente, name='historico_evolucoes_paciente'),
]
