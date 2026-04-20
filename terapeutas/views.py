from django.shortcuts import get_object_or_404, redirect, render
from core.decorators import role_required
from .forms import TerapeutaForm
from .models import Terapeuta


@role_required('recepcao', 'coordenacao', 'terapeuta')
def terapeuta_list(request):
    busca = request.GET.get('q', '')
    terapeutas = Terapeuta.objects.all().prefetch_related('especialidades')
    if request.user.role == 'terapeuta':
        terapeutas = terapeutas.filter(usuario=request.user)
    if busca:
        terapeutas = terapeutas.filter(nome__icontains=busca)
    return render(request, 'terapeutas/list.html', {'terapeutas': terapeutas, 'busca': busca})


@role_required('recepcao', 'coordenacao')
def terapeuta_create(request):
    form = TerapeutaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('terapeuta_list')
    return render(request, 'terapeutas/form.html', {'form': form, 'titulo': 'Novo terapeuta'})


@role_required('recepcao', 'coordenacao')
def terapeuta_update(request, pk):
    terapeuta = get_object_or_404(Terapeuta, pk=pk)
    form = TerapeutaForm(request.POST or None, instance=terapeuta)
    if form.is_valid():
        form.save()
        return redirect('terapeuta_list')
    return render(request, 'terapeutas/form.html', {'form': form, 'titulo': 'Editar terapeuta'})


@role_required('recepcao', 'coordenacao')
def terapeuta_delete(request, pk):
    terapeuta = get_object_or_404(Terapeuta, pk=pk)
    if request.method == 'POST':
        terapeuta.delete()
        return redirect('terapeuta_list')
    return render(request, 'confirm_delete.html', {'obj': terapeuta, 'titulo': 'Excluir terapeuta'})
