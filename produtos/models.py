from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_lenght=100)
    descrição = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    data_criacao = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
