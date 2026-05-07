from datetime import date, datetime
from django.shortcuts import render
from core.decorators import role_required
from agenda.models import Atendimento
from terapeutas.models import Terapeuta


@role_required('coordenacao')
def produtividade_view(request):
    hoje = date.today()
    inicio = request.GET.get('inicio') or hoje.replace(day=1).isoformat()
    fim = request.GET.get('fim') or hoje.isoformat()
    inicio_dt = datetime.strptime(inicio, '%Y-%m-%d').date()
    fim_dt = datetime.strptime(fim, '%Y-%m-%d').date()

    dados = []
    terapeutas = Terapeuta.objects.all().prefetch_related()
    for terapeuta in terapeutas:
        atendimentos = terapeuta.atendimentos.filter(data__range=[inicio_dt, fim_dt])
        total_agendado = atendimentos.count()
        realizados = atendimentos.filter(status_presenca=Atendimento.PRESENTE).count()
        faltas = atendimentos.filter(status_presenca=Atendimento.FALTA).count()
        faltas_justificadas = atendimentos.filter(status_presenca=Atendimento.FALTA_JUSTIFICADA).count()
        extras = atendimentos.filter(tipo=Atendimento.EXTRA).count()
        produtividade = round((realizados / total_agendado) * 100, 2) if total_agendado else 0
        dados.append({
            'terapeuta': terapeuta,
            'total_agendado': total_agendado,
            'realizados': realizados,
            'faltas': faltas,
            'faltas_justificadas': faltas_justificadas,
            'extras': extras,
            'produtividade': produtividade,
        })

    return render(request, 'relatorios/produtividade.html', {
        'dados': dados,
        'inicio': inicio,
        'fim': fim,
    })
