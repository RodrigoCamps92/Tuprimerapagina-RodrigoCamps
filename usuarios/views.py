from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django import forms

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Cuenta creada con éxito!')
            return redirect('blog:post_list')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        u = request.user
        u.first_name = request.POST.get('first_name', '')
        u.last_name  = request.POST.get('last_name', '')
        u.email      = request.POST.get('email', u.email)
        u.save()
        messages.success(request, 'Perfil actualizado.')
        return redirect('usuarios:perfil')
    return render(request, 'usuarios/editar_perfil.html')