from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm, PerfilForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('usuarios:login')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def perfil_view(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente!')
            return redirect('usuarios:perfil')
    else:
        form = PerfilForm(instance=request.user.perfil)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})