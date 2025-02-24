from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProdutoViewSet, 
    painel, 
    editar_produto,
    adicionar_produto,
    excluir_produto
    )

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('painel/', painel, name='painel'),
    path('editar/<int:id>/', editar_produto, name='editar'),
    path('adicionar/', adicionar_produto, name='adicionar_produto'),
    path('excluir/<int:id>/', excluir_produto, name='excluir'),
    path('api/', include(router.urls)),
]