from datetime import date
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import render
from agenda.models import Atendimento
from pacientes.models import Paciente
from terapeutas.models import Terapeuta
from users.models import User


@login_required
def dashboard(request):
    hoje = date.today()
    total_pacientes = Paciente.objects.count()
    total_terapeutas = Terapeuta.objects.count()
    total_usuarios = User.objects.count()
    atendimentos_hoje = Atendimento.objects.filter(data=hoje).count()
    totais_status = Atendimento.objects.aggregate(
        presentes=Count('id', filter=Q(status_presenca=Atendimento.PRESENTE)),
        faltas=Count('id', filter=Q(status_presenca=Atendimento.FALTA)),
        justificadas=Count('id', filter=Q(status_presenca=Atendimento.FALTA_JUSTIFICADA)),
        extras=Count('id', filter=Q(tipo=Atendimento.EXTRA)),
    )
    modulos = [
        {'titulo': 'Usuários', 'descricao': 'Cadastro de usuários, perfis e permissões.', 'url': 'user_list', 'roles': ['coordenacao']},
        {'titulo': 'Pacientes', 'descricao': 'Cadastro de crianças, responsáveis e contatos.', 'url': 'paciente_list', 'roles': ['recepcao', 'coordenacao']},
        {'titulo': 'Terapeutas', 'descricao': 'Cadastro de profissionais e especialidades.', 'url': 'terapeuta_list', 'roles': ['recepcao', 'coordenacao']},
        {'titulo': 'Agenda semanal', 'descricao': 'Horários fixos recorrentes de segunda a sexta.', 'url': 'agenda_list', 'roles': ['recepcao', 'coordenacao']},
        {'titulo': 'Presenças', 'descricao': 'Lista diária para marcar presente, falta e justificativa.', 'url': 'atendimento_diario', 'roles': ['recepcao', 'coordenacao', 'terapeuta']},
        {'titulo': 'Atendimento extra', 'descricao': 'Cadastro de encaixes em horários vagos.', 'url': 'atendimento_extra_create', 'roles': ['recepcao', 'coordenacao', 'terapeuta']},
        {'titulo': 'Relatórios', 'descricao': 'Produtividade por terapeuta e período.', 'url': 'produtividade_view', 'roles': ['coordenacao']},
    ]
    modulos_visiveis = [mod for mod in modulos if request.user.role in mod['roles']]
    context = {
        'hoje': hoje,
        'total_pacientes': total_pacientes,
        'total_terapeutas': total_terapeutas,
        'total_usuarios': total_usuarios,
        'atendimentos_hoje': atendimentos_hoje,
        'totais_status': totais_status,
        'modulos_visiveis': modulos_visiveis,
    }
    return render(request, 'core/dashboard.html', context)
