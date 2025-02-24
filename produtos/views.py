from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseNotAllowed
from .models import Produto
from rest_framework import viewsets
from .serializers import ProdutoSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.core.paginator import Paginator

from django.core.paginator import Paginator

@login_required
def painel(request):
    nome_filtro = request.GET.get('nome', '')
    
    produtos = Produto.objects.all().order_by('-data_criacao')
    
    if nome_filtro:
        produtos = produtos.filter(nome__icontains=nome_filtro)
    
    paginator = Paginator(produtos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'painel.html', {
        'page_obj': page_obj,
        'nome_filtro': nome_filtro 
    })

@login_required
def editar_produto(request, id):
    if not request.user.groups.filter(name='Supervisor').exists():
        return HttpResponseForbidden("Acesso negado: você não é um Supervisor")
    
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descrição')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        try:
            if preco:
                preco = float(preco)
                if preco < 0:
                    raise ValueError("O preço não pode ser negativo.")
                if preco > 99999999.99:
                    raise ValueError("O preço não pode ser maior que 99.999.999,99.")
        except ValueError as e:
            messages.error(request, f'Erro nos valores informados: {str(e)}')
            return redirect('editar_produto', id=id)

        try:
            quantidade = int(quantidade)
            if quantidade < 0:
                raise ValueError("A quantidade não pode ser negativa.")
        except ValueError as e:
            messages.error(request, f'Erro nos valores informados: {str(e)}')
            return redirect('editar_produto', id=id)

        produto.nome = nome
        produto.descrição = descricao
        produto.preco = preco
        produto.quantidade = quantidade
        produto.save()

        messages.success(request, 'Produto atualizado com sucesso!')
        return redirect('painel')

    return render(request, 'editar_produto.html', {'produto': produto})


@login_required
def adicionar_produto(request):
    if not request.user.groups.filter(name__in=['Analista', 'Supervisor']).exists():
        return HttpResponseForbidden("Acesso negado")
    
    if request.method == 'POST':
        try:
            nome = request.POST.get('nome')
            descricao = request.POST.get('descrição')
            preco = request.POST.get('preco')
            quantidade = request.POST.get('quantidade')

            if len(nome) > 150:
                messages.error(request, 'O nome do produto não pode ter mais que 150 caracteres.')
                return redirect('adicionar_produto')

            if len(descricao) < 3:
                messages.error(request, 'A descrição precisa ter pelo menos 3 caracteres.')
                return redirect('adicionar_produto')
            if len(descricao) > 1000:
                messages.error(request, 'A descrição não pode ter mais que 1000 caracteres.')
                return redirect('adicionar_produto')

            try:
                preco = float(preco)
                if preco < 0:
                    raise ValueError("O preço não pode ser negativo.")
                if preco > 99999999.99: 
                    raise ValueError("O preço não pode ser maior que 99.999.999,99.")
            except ValueError as e:
                messages.error(request, f'Erro nos valores informados no preço: {str(e)}')
                return redirect('adicionar_produto')

            try:
                quantidade = int(quantidade)
                if quantidade < 0:
                    raise ValueError("A quantidade não pode ser negativa.")
            except ValueError as e:
                messages.error(request, f'Erro nos valores informados na quantidade: {str(e)}')
                return redirect('adicionar_produto')

            novo_produto = Produto(
                nome=nome,
                descrição=descricao,
                preco=preco,
                quantidade=quantidade,
                usuario=request.user
            )
            novo_produto.save()
            messages.success(request, 'Produto adicionado com sucesso!')
            return redirect('painel')

        except Exception as e:
            messages.error(request, f'Erro ao adicionar produto: {str(e)}')
    
    return render(request, 'adicionar_produto.html')

@login_required
def excluir_produto(request, id):
    if not request.user.groups.filter(name='Supervisor').exists():
        return HttpResponseForbidden("Acesso negado")
    
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('painel')
    
    return HttpResponseNotAllowed(['POST'])

class ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

