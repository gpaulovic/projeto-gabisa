from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Reserva
from .forms import ReservaForm
from brinquedos.models import Brinquedo
from django.contrib.auth.decorators import login_required

@login_required
def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})

@login_required
def detalhes_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, 'reservas/detalhes_reserva.html', {'reserva': reserva})

@login_required
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva criada com sucesso.')
            return redirect('reservas:listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/criar_reserva.html', {'form': form})

@login_required
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva editada com sucesso.')
            return redirect('reservas:listar_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/editar_reserva.html', {'form': form, 'reserva': reserva})

@login_required
def excluir_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.delete()
    messages.success(request, 'Reserva excluída com sucesso.')
    return redirect('reservas:listar_reservas')
