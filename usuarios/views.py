from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistrarForm

def registrar(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('painel')
    else:
        form = RegistrarForm()
    return render(request, 'registrar.html', {'form: form'})

def fazer_login(request):
    pass 

def fazer_logout(request):
    logout(request)
    return redirect('login')


