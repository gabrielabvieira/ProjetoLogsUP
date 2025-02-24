from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistrarForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def registrar(request):
    if request.user.is_authenticated:
        return redirect('painel') 

    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('painel')
        else:
            messages.error(request, 'Erro ao cadastrar, verifique os dados.')
    else:
        form = RegistrarForm()
    
    return render(request, 'registrar.html', {'form': form})

def fazer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('painel')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def fazer_logout(request):
    logout(request)
    return redirect('login')


