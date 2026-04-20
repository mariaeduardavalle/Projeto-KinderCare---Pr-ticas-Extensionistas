from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from core.decorators import role_required
from agenda.models import Atendimento
from pacientes.models import Paciente
from .forms import EvolucaoForm
from .models import Evolucao


@role_required('recepcao', 'coordenacao', 'terapeuta')
def evolucao_create_or_update(request, atendimento_pk):
    atendimento = get_object_or_404(Atendimento, pk=atendimento_pk)
    if request.user.role == 'terapeuta' and atendimento.terapeuta.usuario_id != request.user.id:
        messages.error(request, 'Você só pode registrar evoluções dos seus próprios atendimentos.')
        return redirect('atendimento_diario')
    evolucao, _ = Evolucao.objects.get_or_create(atendimento=atendimento)
    form = EvolucaoForm(request.POST or None, instance=evolucao)
    if form.is_valid():
        form.save()
        return redirect('historico_evolucoes_paciente', paciente_pk=atendimento.paciente.pk)
    return render(request, 'evolucoes/form.html', {'form': form, 'atendimento': atendimento})


@role_required('recepcao', 'coordenacao', 'terapeuta')
def historico_evolucoes_paciente(request, paciente_pk):
    paciente = get_object_or_404(Paciente, pk=paciente_pk)
    evolucoes = Evolucao.objects.filter(atendimento__paciente=paciente).select_related('atendimento', 'atendimento__terapeuta')
    if request.user.role == 'terapeuta':
        evolucoes = evolucoes.filter(atendimento__terapeuta__usuario=request.user)
    return render(request, 'evolucoes/historico.html', {'paciente': paciente, 'evolucoes': evolucoes})
