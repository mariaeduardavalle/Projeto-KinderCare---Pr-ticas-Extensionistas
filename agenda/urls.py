from django.urls import path
from . import views

urlpatterns = [
    path('', views.agenda_list, name='agenda_list'),
    path('novo/', views.agenda_create, name='agenda_create'),
    path('<int:pk>/editar/', views.agenda_update, name='agenda_update'),
    path('<int:pk>/excluir/', views.agenda_delete, name='agenda_delete'),
    path('gerar-atendimentos/', views.gerar_atendimentos, name='gerar_atendimentos'),
    path('atendimentos/', views.atendimento_diario, name='atendimento_diario'),
    path('atendimentos/<int:pk>/presenca/', views.registrar_presenca, name='registrar_presenca'),
    path('atendimentos/extra/novo/', views.atendimento_extra_create, name='atendimento_extra_create'),
]
