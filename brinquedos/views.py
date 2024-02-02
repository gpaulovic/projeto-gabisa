from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Brinquedo
from .forms import BrinquedoForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_brinquedos(request):
    brinquedos = Brinquedo.objects.all()
    return render(request, 'brinquedos/listar_brinquedos.html', {'brinquedos': brinquedos})

@login_required
def detalhes_brinquedo(request, brinquedo_id):
    brinquedo = get_object_or_404(Brinquedo, pk=brinquedo_id)
    return render(request, 'brinquedos/detalhes_brinquedo.html', {'brinquedo': brinquedo})

@login_required
def criar_brinquedo(request):
    if request.method == 'POST':
        form = BrinquedoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brinquedo criado com sucesso.')
            return redirect('brinquedos:listar_brinquedos')
    else:
        form = BrinquedoForm()
    return render(request, 'brinquedos/criar_brinquedo.html', {'form': form})

@login_required
def editar_brinquedo(request, brinquedo_id):
    brinquedo = get_object_or_404(Brinquedo, pk=brinquedo_id)
    if request.method == 'POST':
        form = BrinquedoForm(request.POST, instance=brinquedo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brinquedo editado com sucesso.')
            return redirect('brinquedos:listar_brinquedos')
    else:
        form = BrinquedoForm(instance=brinquedo)
    return render(request, 'brinquedos/editar_brinquedo.html', {'form': form, 'brinquedo': brinquedo})

@login_required
def excluir_brinquedo(request, brinquedo_id):
    brinquedo = get_object_or_404(Brinquedo, pk=brinquedo_id)
    brinquedo.delete()
    messages.success(request, 'Brinquedo excluído com sucesso.')
    return redirect('brinquedos:listar_brinquedos')
