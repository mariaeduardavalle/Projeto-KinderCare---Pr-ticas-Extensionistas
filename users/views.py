from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from core.decorators import role_required
from .forms import UserForm

User = get_user_model()


@role_required('coordenacao')
def user_list(request):
    busca = request.GET.get('q', '')
    usuarios = User.objects.all().order_by('first_name', 'username')
    if busca:
        usuarios = usuarios.filter(username__icontains=busca) | usuarios.filter(first_name__icontains=busca) | usuarios.filter(last_name__icontains=busca)
    return render(request, 'users/list.html', {'usuarios': usuarios, 'busca': busca})


@role_required('coordenacao')
def user_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'users/form.html', {'form': form, 'titulo': 'Novo usuário'})


@role_required('coordenacao')
def user_update(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'users/form.html', {'form': form, 'titulo': 'Editar usuário', 'usuario': usuario})


@role_required('coordenacao')
def user_delete(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('user_list')
    return render(request, 'confirm_delete.html', {'obj': usuario, 'titulo': 'Excluir usuário'})
