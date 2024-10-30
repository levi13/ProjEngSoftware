# schedule/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def agendamentos_list(request):
    query = request.GET.get('q')
    agendamentos = Agendamento.objects.filter(usuario=request.user)
    if query:
        agendamentos = agendamentos.filter(descricao__icontains=query)
    return render(request, 'schedule/agendamentos_list.html', {'agendamentos': agendamentos})


def agendamento_create(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user  # Associando o usuário atual
            agendamento.save()
            messages.success(request, 'Agendamento criado com sucesso!')
            return redirect('agendamentos_list')
        else:
            messages.error(request, 'Erro ao criar o agendamento.')
    else:
        form = AgendamentoForm()
    return render(request, 'schedule/agendamento_form.html', {'form': form})

def agendamento_edit(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento atualizado com sucesso!')
            return redirect('agendamentos_list')
        else:
            messages.error(request, 'Erro ao atualizar o agendamento.')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'schedule/agendamento_form.html', {'form': form, 'editar': True})

def agendamento_delete(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    if request.method == 'POST':
        agendamento.delete()
        messages.success(request, 'Agendamento excluído com sucesso!')
        return redirect('agendamentos_list')
    return render(request, 'schedule/agendamento_confirm_delete.html', {'agendamento': agendamento})


def agendamento_create(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user
            agendamento.save()
            messages.success(request, 'Agendamento criado com sucesso!')
            return redirect('agendamentos_list')
        else:
            messages.error(request, 'Erro ao criar o agendamento.')
    else:
        form = AgendamentoForm()
    return render(request, 'schedule/agendamento_form.html', {'form': form})

def agendamento_edit(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento atualizado com sucesso!')
            return redirect('agendamentos_list')
        else:
            messages.error(request, 'Erro ao atualizar o agendamento.')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'schedule/agendamento_form.html', {'form': form})

def agendamento_delete(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    if request.method == 'POST':
        agendamento.delete()
        messages.success(request, 'Agendamento excluído com sucesso!')
        return redirect('agendamentos_list')
    return render(request, 'schedule/agendamento_confirm_delete.html', {'agendamento': agendamento})

