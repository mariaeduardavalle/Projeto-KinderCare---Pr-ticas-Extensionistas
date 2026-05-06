from datetime import date, datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from core.decorators import role_required
from .forms import AgendaSemanalForm, AtendimentoExtraForm, PresencaForm
from .models import AgendaSemanal, Atendimento


@role_required('recepcao', 'coordenacao', 'terapeuta')
def agenda_list(request):
    agendas = AgendaSemanal.objects.select_related().all()
    # if request.user.role == 'terapeuta':
    #     agendas = agendas.filter(terapeuta__usuario=request.user)
    return render(request, 'agenda/list.html', {'agendas': agendas})


@role_required('recepcao', 'coordenacao')
def agenda_create(request):
    form = AgendaSemanalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('agenda_list')
    return render(request, 'agenda/form.html', {'form': form, 'titulo': 'Novo agendamento fixo'})


@role_required('recepcao', 'coordenacao')
def agenda_update(request, pk):
    agenda = get_object_or_404(AgendaSemanal, pk=pk)
    form = AgendaSemanalForm(request.POST or None, instance=agenda)
    if form.is_valid():
        form.save()
        return redirect('agenda_list')
    return render(request, 'agenda/form.html', {'form': form, 'titulo': 'Editar agendamento fixo'})


@role_required('recepcao', 'coordenacao')
def agenda_delete(request, pk):
    agenda = get_object_or_404(AgendaSemanal, pk=pk)
    if request.method == 'POST':
        agenda.delete()
        return redirect('agenda_list')
    return render(request, 'confirm_delete.html', {'obj': agenda, 'titulo': 'Excluir agendamento'})


@role_required('recepcao', 'coordenacao')
def gerar_atendimentos(request):
    if request.method == 'POST':
        data_inicial = datetime.strptime(
            request.POST['data_inicial'], '%Y-%m-%d').date()
        data_final = datetime.strptime(
            request.POST['data_final'], '%Y-%m-%d').date()
        Atendimento.gerar_atendimentos_periodo(data_inicial, data_final)
        messages.success(
            request, 'Atendimentos gerados com sucesso para o período informado.')
        return redirect('atendimento_diario')
    return render(request, 'agenda/gerar_atendimentos.html')


@role_required('recepcao', 'coordenacao', 'terapeuta')
def atendimento_diario(request):
    data_ref = request.GET.get('data')
    if data_ref:
        data_ref = datetime.strptime(data_ref, '%Y-%m-%d').date()
    else:
        data_ref = date.today()
    atendimentos = Atendimento.objects.filter(data=data_ref).select_related()
    # if request.user.role == 'terapeuta':
    #     atendimentos = atendimentos.filter(terapeuta__usuario=request.user)
    return render(request, 'agenda/atendimento_diario.html', {'atendimentos': atendimentos, 'data_ref': data_ref})


@role_required('recepcao', 'coordenacao', 'terapeuta')
def registrar_presenca(request, pk):
    atendimento = get_object_or_404(Atendimento, pk=pk)
    # if request.user.role == 'terapeuta' and atendimento.terapeuta.usuario_id != request.user.id:
    #     messages.error(request, 'Você só pode registrar presença dos seus próprios atendimentos.')
    #     return redirect('atendimento_diario')
    form = PresencaForm(request.POST or None, instance=atendimento)
    if form.is_valid():
        form.save()
        return redirect(f'/agenda/atendimentos/?data={atendimento.data}')
    return render(request, 'agenda/presenca_form.html', {'form': form, 'atendimento': atendimento})


@role_required('recepcao', 'coordenacao', 'terapeuta')
def atendimento_extra_create(request):
    form = AtendimentoExtraForm(request.POST or None)
    if form.is_valid():
        atendimento = form.save(commit=False)
        # if request.user.role == 'terapeuta' and atendimento.terapeuta.usuario_id != request.user.id:
        #     messages.error(request, 'Você só pode criar encaixes vinculados ao seu próprio cadastro de terapeuta.')
        #     return redirect('atendimento_diario')
        atendimento.tipo = Atendimento.EXTRA
        atendimento.status_presenca = Atendimento.AGENDADO
        atendimento.save()
        messages.success(request, 'Atendimento extra cadastrado com sucesso.')
        return redirect('atendimento_diario')
    return render(request, 'agenda/form.html', {'form': form, 'titulo': 'Novo atendimento extra'})
